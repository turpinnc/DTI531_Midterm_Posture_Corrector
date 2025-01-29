from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    # Simulate temperature reading
    temp = round(random.uniform(20.0, 25.0), 1)
    
    return jsonify({
        "temperature": temp,
        "unit": "celsius",
        "timestamp": datetime.now().isoformat(),
        "sensor": "room_1"
    })

@app.route('/api/temperature/room/<room_id>', methods=['GET'])
def get_room_temperature(room_id):
    # Simulate different temperature ranges for different rooms
    temp_ranges = {
        "room_1": (20.0, 22.0),
        "room_2": (21.0, 23.0),
        "room_3": (22.0, 24.0)
    }
    
    if room_id not in temp_ranges:
        return jsonify({"error": "Room not found"}), 404
    
    min_temp, max_temp = temp_ranges[room_id]
    temp = round(random.uniform(min_temp, max_temp), 1)
    
    return jsonify({
        "temperature": temp,
        "unit": "celsius",
        "room": room_id,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)