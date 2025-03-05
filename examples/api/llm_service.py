# llm_service.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Configure the Gemini API
genai.configure(api_key=API_KEY)

# 3. Initialize the generative model
#    Replace "gemini-1.5-flash" with the exact model name you want
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_feedback(posture_state):
    """
    Generates posture correction advice for the given posture_state
    using a Gemini model (without the palm.chat approach).
    """
    prompt = (
        f"Provide posture correction advice for someone who is demonstrating: {posture_state}. "
        "Be concise and friendly."
    )

    try:
        # 4. Use model.generate_content(...) with a GenerationConfig
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.7
            )
        )
        # 5. Extract and return the generated text
        return response.text

    except Exception as e:
        return f"Error generating feedback: {str(e)}"


