from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from React frontend


# Example endpoint for reviews
@app.route("/api/reviews")
def get_reviews():
    mock_reviews = [
        {"username": "Alice", "rating": 5, "comment": "Excellent service!", "sentiment": "Positive"},
        {"username": "Bob", "rating": 3, "comment": "Average experience", "sentiment": "Neutral"},
        {"username": "Charlie", "rating": 1, "comment": "Very poor support", "sentiment": "Negative"},
    ]
    return jsonify(mock_reviews)

# Example endpoint for sentiment summary
@app.route("/api/sentiment-summary")
def get_sentiment_summary():
    data = {
        "weeks": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "scores": [0.75, 0.82, 0.68, 0.9]
    }
    return jsonify(data)

# Example endpoint for competitor data
@app.route("/api/competitors")
def get_competitors():
    data = [
        {"name": "Business A", "rating": 4.5},
        {"name": "Business B", "rating": 4.0},
        {"name": "Your Business", "rating": 4.2},
    ]
    return jsonify(data)

@app.route("/")
def home():
    return "<h1>Flask API is running!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
