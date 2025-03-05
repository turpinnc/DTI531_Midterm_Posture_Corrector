# client.py
import requests
import dashboard
from pynput import keyboard
from queue import Queue, Empty
import time

SERVER_URL = "http://127.0.0.1:5000/keypress"

key_to_posture = {
    "g": "Good Posture",
    "f": "Forward Lean",
    "s": "Slouched Back",
    "l": "Leaning to One Side"
}

# Thread-safe queue for posture updates
event_queue = Queue()

def analyze_posture_via_server(posture_state):
    """
    Sends posture_state to the server, gets feedback,
    and places (posture_state, feedback) into event_queue.
    """
    print(f"[CLIENT] DEBUG: Sending POST with posture_state={posture_state}")
    try:
        response = requests.post(SERVER_URL, json={"posture_state": posture_state})
        if response.status_code == 200:
            data = response.json()
            feedback = data.get('feedback', 'No feedback')
            print(f"[CLIENT] DEBUG: Received from server -> {feedback}")
            # Put the event into the queue for the main thread to process
            event_queue.put((posture_state, feedback))
        else:
            print(f"[CLIENT] Server Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"[CLIENT] Error connecting to server: {e}")

def on_press(key):
    """
    Callback for pynput's keyboard listener (runs on a separate thread).
    We just detect keys, do NOT call Matplotlib here.
    """
    try:
        k = key.char.lower()
        print(f"[CLIENT] DEBUG: Key pressed -> {k}")
    except:
        # Special key pressed, ignore
        return

    if k == 'esc':
        print("[CLIENT] Exiting client.")
        return False  # Stop listener

    posture_state = key_to_posture.get(k, "Unknown")
    print(f"[CLIENT] DEBUG: posture_state={posture_state}")
    if posture_state != "Unknown":
        analyze_posture_via_server(posture_state)

if __name__ == "__main__":
    print("[CLIENT] AlignMate Client Running! Press G, F, S, L to simulate posture. ESC to exit.")

    # Start pynput listener in its own thread
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Main thread loop: fetch posture updates from event_queue and update Matplotlib
    try:
        while listener.is_alive():
            try:
                posture_state, feedback = event_queue.get(timeout=0.1)
                # Now we can safely call Matplotlib on the main thread
                dashboard.update_dashboard(posture_state, feedback)
            except Empty:
                pass  # No event in queue, just loop
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("[CLIENT] KeyboardInterrupt. Exiting.")
    listener.join()



