# analysis.py
import llm_service

def analyze_posture(posture_state):
    bad_postures = ["Forward Lean", "Slouched Back", "Leaning to One Side"]
    
    print("DEBUG: In analyze_posture with:", posture_state)  # <-- Debug

    if posture_state in bad_postures:
        print("DEBUG: Detected bad posture, calling LLM service...")  # <-- Debug
        feedback = llm_service.generate_feedback(posture_state)
        return ("bad", feedback)
    elif posture_state == "Good Posture":
        return ("good", "Great job! Keep maintaining this posture!")
    else:
        return ("unknown", "We couldn't classify your posture.")


