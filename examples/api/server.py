# server.py
from flask import Flask, request, jsonify
import analysis  # Import your analysis module
# analysis internally imports llm_service if needed

app = Flask(__name__)

@app.route('/keypress', methods=['POST'])
def process_keypress():
    """
    Receives JSON with 'posture_state',
    calls analysis (which uses the LLM for bad postures),
    and returns the feedback to the client.
    """
    data = request.json
    posture_state = data.get('posture_state')

    if not posture_state:
        return jsonify({'error': 'No posture_state provided'}), 400

    # Call analysis to classify posture and get feedback
    analyzed_state, feedback = analysis.analyze_posture(posture_state)
    
    # For debugging, log what we got:
    print(f"Posture: {posture_state}, Analyzed: {analyzed_state}, Feedback: {feedback}")

    # Return JSON with the feedback
    return jsonify({
        'analyzed_state': analyzed_state,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)


 
