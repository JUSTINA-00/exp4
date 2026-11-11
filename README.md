# Personalized Recommendation System

A simple beginner-level Flask project. It collects user preferences, scores a small list of learning resources, displays the top five, and accepts feedback.

## Requirements
- Python 3.x
- Flask
- VS Code (or any code editor)

## Run the project

1. Open a terminal in this project folder.
2. (Optional) Create a virtual environment:

   python -m venv venv

3. Activate it on Windows:

   venv\Scripts\activate

4. Install Flask:

   pip install -r requirements.txt

5. Run the application:

   python app.py

6. Open this address:

   http://127.0.0.1:5000

## Files
- app.py: Flask app and simple recommendation/ranking logic
- templates/index.html: HTML and CSS user interface
- requirements.txt: Required Python package

## Notes
- This version uses simple preference-based rules and a small built-in sample list.
- It does not call GPT-4 or any paid API.
- Feedback is kept in the browser session for this simple demonstration.
- Permanent saving of recommendation results is not implemented, matching the supplied experiment description.
