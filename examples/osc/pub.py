from pythonosc import udp_client
import argparse
import random
import time

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    # Create OSC client
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    try:
        while True:
            # Generate random temperature between 20 and 25
            temperature = round(random.uniform(20.0, 25.0), 1)
            
            # Send temperature reading
            client.send_message("/sensor/temperature", temperature)
            print(f"Sent temperature: {temperature}°C")
            
            # Send multiple values as an example
            sensor_bundle = [temperature, random.randint(40, 60)]  # temp and humidity
            client.send_message("/sensor/bundle", sensor_bundle)
            print(f"Sent sensor bundle: {sensor_bundle}")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping sender...")