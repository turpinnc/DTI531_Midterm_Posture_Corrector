import keyboard  # Library to detect key presses
import analysis  # Import the analysis module
import dashboard  # Import the dashboard for visualization

def capture_key_input():
    """Listens for key presses and maps them to posture states."""
    key_to_posture = {
        "g": "Good Posture",
        "f": "Forward Lean",
        "s": "Slouched Back",
        "l": "Leaning to One Side"
    }

    print("\nAlignMate Running! Press a key to simulate posture:")
    print("   G = Good Posture")
    print("   F = Forward Lean")
    print("   S = Slouched Back")
    print("   L = Leaning to One Side\n")
    print("Press 'ESC' to exit.")

    while True:
        event = keyboard.read_event()  # Detect key press
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name.lower()  # Convert to lowercase

            if key == "esc":
                print("\nExiting AlignMate. Stay aligned! 😊")
                break  # Exit the loop

            posture_state = key_to_posture.get(key, "Unknown")

            if posture_state != "Unknown":
                print(f"\n✅ Detected posture: {posture_state}")
                handle_posture_input(posture_state)  # Send to analysis

def handle_posture_input(posture_state):
    """Processes the captured posture and updates the UI."""
    analyzed_state, feedback = analysis.analyze_posture(posture_state)
    
    #Send data to the UI Dashboard
    dashboard.update_dashboard(posture_state, feedback)

if __name__ == "__main__":
    capture_key_input()
