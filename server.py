from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

def run_emotion_detection():
@app.route("/emotionDetector")
def sent_detector():
    text_to_detect = request.args.get('textToAnalyze')
    formated_response = emotion_detector(text_to_detect)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
        page over the Flask channel
    return render_template('index.html')
if __name__ == "__main__":

run_emotion_detection()