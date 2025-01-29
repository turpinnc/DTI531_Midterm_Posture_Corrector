# receiver.py
from pythonosc import dispatcher
from pythonosc import osc_server
import argparse
import math

def process_sensor_data(address, *args):
    print(f"Received sensor data at {address}: {args}")

def process_temperature(address, *args):
    if args and len(args) > 0:
        temp = args[0]
        print(f"Temperature reading: {temp}°C")
        # You could add additional processing here

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
        help="The ip to listen on")
    parser.add_argument("--port", type=int, default=5005,
        help="The port to listen on")
    args = parser.parse_args()

    # Set up dispatcher
    dispatch = dispatcher.Dispatcher()
    dispatch.map("/sensor/*", process_sensor_data)
    dispatch.map("/sensor/temperature", process_temperature)

    # Start OSC server
    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatch)
    print(f"Serving on {server.server_address}")
    server.serve_forever()