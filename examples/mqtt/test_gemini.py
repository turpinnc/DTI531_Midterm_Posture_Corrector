import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables (if needed)
load_dotenv()

# Configure the Gemini API using the environment variable
print(os.environ["GEMINI_API_KEY"])
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain what MQTT is...")
print(response.text)












