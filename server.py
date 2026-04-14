"""
This module defines a Flask web application for Emotion Detection.
It receives text input from the user and returns the predicted emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint to analyze the emotion of the provided text.
    Retrieves 'textToAnalyze' from request args and returns formatted emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Menangani input kosong (Error Handling)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format output jika sukses
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Endpoint to render the main index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)