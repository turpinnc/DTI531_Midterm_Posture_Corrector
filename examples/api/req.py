import requests
import json

def get_general_temperature():
    """Get temperature from the general endpoint"""
    response = requests.get('http://127.0.0.1:5000/api/temperature')
    return response.json()

def get_room_temperature(room_id):
    """Get temperature for a specific room"""
    response = requests.get(f'http://127.0.0.1:5000/api/temperature/room/{room_id}')
    return response.json()

def main():
    # Get general temperature
    print("\nGeneral temperature reading:")
    result = get_general_temperature()
    print(json.dumps(result, indent=2))

    # Get temperature for each room
    for room_id in ['room_1', 'room_2', 'room_3']:
        print(f"\nTemperature for {room_id}:")
        result = get_room_temperature(room_id)
        print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
