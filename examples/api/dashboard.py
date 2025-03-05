# dashboard.py
import matplotlib.pyplot as plt
import textwrap  # Import textwrap at the top
# Global list to store posture history
posture_history = []

def update_dashboard(posture_state, feedback):
    """
    1) Updates a persistent window for the posture trend.
    2) Pops up a separate window to briefly display the LLM feedback.
    """
    # Append the current posture state
    posture_history.append(posture_state)
    
    # Map posture to numeric for plotting
    mapping = {
        "Good Posture": 1,
        "Forward Lean": 0,
        "Slouched Back": 0,
        "Leaning to One Side": 0
    }
    trend = [mapping.get(state, -1) for state in posture_history]
    
    # -------------------------
    # A) Update the Trend Graph
    # -------------------------
    fig_trend = plt.figure("Posture Trend")
    plt.clf()  # Clear the figure
    plt.plot(trend, marker='o', linestyle='-', color='blue')
    plt.ylim(-1, 2)
    plt.xlabel("Time (Key Press Count)")
    plt.ylabel("Posture (1 = Good, 0 = Bad, -1 = Unknown)")
    plt.title("Posture Trend Over Time")
    plt.draw()
    plt.pause(0.1)

    # -------------------------------
    # B) Show LLM Feedback in a Pop-Up
    # -------------------------------
    # Wrap the feedback text so it doesn't overlap or get cut off
    wrapped_feedback = textwrap.fill(feedback, width=60)  # adjust width as needed

    fig_feedback = plt.figure("LLM Advice", figsize=(8, 6))
    plt.clf()
    plt.axis('off')
    plt.text(0.5, 0.5, wrapped_feedback, fontsize=10, ha='center', va='center', wrap=True)
    plt.title("Posture Advice", fontsize=14)
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)  # Display for 2 seconds
    plt.close(fig_feedback)


import re

def clean_feedback(text):
    # Remove bullet markers at the beginning of lines
    text = re.sub(r'^\*\s*', '', text, flags=re.MULTILINE)
    # Remove asterisks used for bold or emphasis
    text = re.sub(r'\*+', '', text)
    return text.strip()

# Then, in your update_dashboard function, use:
wrapped_feedback = textwrap.fill(clean_feedback(feedback), width=60)
