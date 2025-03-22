from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import os

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

app = Flask(__name__)

# File to store sentiment results
DATA_FILE = "sentiments.json"

# Function to load stored data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        sentiment_score = analyzer.polarity_scores(text)['compound']

        if sentiment_score >= 0.05:
            sentiment = "Positive"
        elif sentiment_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Save to JSON instead of MySQL
        sentiment_data = load_data()
        sentiment_data.append({"text": text, "sentiment": sentiment, "score": sentiment_score})
        save_data(sentiment_data)

        return render_template('result.html', text=text, sentiment=sentiment, score=sentiment_score)

@app.route('/history')
def history():
    sentiment_data = load_data()
    return jsonify(sentiment_data)

if __name__ == '__main__':
    app.run(debug=True)