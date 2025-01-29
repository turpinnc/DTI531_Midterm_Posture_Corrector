import paho.mqtt.client as mqtt
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API using the environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define the callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        # Subscribe to the desired topic
        client.subscribe("nicolehomework/mymessage")
    else:
        print(f"Connection failed with code {rc}")

# Define the callback for when a message is received
def on_message(client, userdata, msg):
    message_payload = msg.payload.decode()
    print(f"Received message on topic {msg.topic}: {message_payload}")

    # Construct the prompt for the generative model
    prompt = (
        f"Explain the following sensor data in simple terms so a non-technical person could understand: {message_payload}"
    )

    try:
        # Make a request to the generative model
        response = model.generate_content(prompt)

        # Extract and print the generated text
        analysis = response.text.strip() if response and hasattr(response, 'text') else "No response"

        print("LLM Analysis:")
        print(analysis)
        print("-" * 50)

    except Exception as e:
        print(f"Error calling generative model: {e}")

# Create the MQTT subscriber client
subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to a public broker
print("Connecting to broker...")
subscriber.connect("test.mosquitto.org", 1883, 60)

# Start the subscriber loop
subscriber.loop_start()

try:
    while True:
        time.sleep(1)  # Keep the program running
except KeyboardInterrupt:
    print("Stopping subscriber...")
    subscriber.loop_stop()
    subscriber.disconnect()



