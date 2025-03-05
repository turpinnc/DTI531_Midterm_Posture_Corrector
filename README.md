#AlignMate – Your Smart Posture Assistant

##Overview

AlignMate is a smart posture assistant that uses a small Flask API, AI-generated feedback, and a visual dashboard to help users improve their posture in real time. The prototype demonstrates device connectivity, ML/LLM data enrichment, and an engaging, user-facing visual component.

#The Problem

Many people suffer from poor posture due to long hours at the desk, which can lead to chronic back pain, neck strain, and decreased productivity. Traditional methods (like printed reminders) often fall short in providing immediate and personalized corrective feedback. AlignMate addresses this by providing real-time, actionable posture advice.

#The Product

AlignMate works by capturing posture data (currently simulated via key presses) from the user. The client sends this data to a Flask server using a REST API. The server then processes the posture data with an analysis module that leverages the Gemini API to generate personalized feedback for both good and poor posture. Finally, a visual dashboard (built with Matplotlib) displays a persistent trend graph alongside a pop-up that shows the AI-generated advice.

#Key Features

Device Connectivity: 
A client captures key presses (using pynput) and communicates with a Flask-based server via REST API.

ML/LLM Data Enrichment: 
The server analyzes the input and calls the Gemini API (using the google-generativeai library) to generate personalized posture advice.

User-Facing Visual Component: 
A dashboard shows a real-time trend graph of posture states and pops up with large, actionable feedback.

Scalability: 
The modular design of the system allows for future enhancements, such as integrating a camera with a Raspberry Pi for real-time posture detection.

#Technology Choices

Our system uses a small web service built with Flask—a lightweight Python framework that acts as a REST API. This API lets our client and server exchange data seamlessly. The client, built using Python and the pynput library, captures key presses to simulate different posture states. The server processes these inputs and uses the Gemini API (via the google-generativeai library) to generate personalized, actionable advice. We display the results using Matplotlib to create clear, visual graphs. All of this runs in a Python virtual environment, ensuring a clean, organized setup with the correct versions of each library.

#Product Description & Reflection

AlignMate is designed to solve a real and common problem: poor posture due to prolonged computer use. It provides immediate, personalized feedback to help users adjust their posture before issues become chronic. Personally, I find this project compelling because I believe in the importance of health and well-being. I’d love to have a tool that not only reminds me to sit up straight but also offers encouraging, actionable advice—making it both useful and engaging. The design is simple and intuitive, yet it leverages modern technologies, ensuring reliability and scalability for future enhancements (like integrating real-time computer vision on a Raspberry Pi).

#Setup Instructions

Clone the Repository:

Open a terminal and run:

git clone https://github.com/yourusername/DTI531_Midterm_Posture_Corrector.git cd DTI531_Midterm_Posture_Corrector

Create & Activate a Virtual Environment:

Run:

python3 -m venv venv

Then activate it:

source venv/bin/activate (On Windows: venv\Scripts\activate)

Install Dependencies:

Run the following command:

pip install flask requests pynput matplotlib python-dotenv google-generativeai

Set Up the Environment Variables:

Create a file named ".env" in the root directory and add the following line:

GEMINI_API_KEY=YOUR_ACTUAL_KEY

Run the Server:

Open a terminal window, navigate to the project folder, and run:

python server.py

You should see a message indicating that the Flask server is running at http://127.0.0.1:5000.

Run the Client:

Open a second terminal window, activate the virtual environment, and run:

python client.py

Follow the on-screen instructions to press G, F, S, or L to simulate different posture states.

The dashboard will update with a trend graph and a pop-up with AI-generated advice.
