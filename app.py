# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper_yelp import reviews_for as yelp_reviews_for
from scraper_google import reviews_for as google_reviews_for
from sentiment import analyze_sentiment, extract_entities, weekly_sentiment_summary
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route("/api/reviews")
def get_reviews():
    source = request.args.get("source", "yelp")  # 'yelp' or 'google'
    q = request.args.get("q", "")               # e.g., "coffee shop, Austin, TX" or text query
    if source == "yelp":
        term, location = (q.split(",",1)[0].strip(), q.split(",",1)[1].strip()) if "," in q else (q, "")
        reviews = yelp_reviews_for(term, location)
    else:
        reviews = google_reviews_for(q)
    reviews = analyze_sentiment(reviews)
    reviews = extract_entities(reviews)
    return jsonify(reviews)

@app.route("/api/sentiment-summary")
def get_summary():
    source = request.args.get("source", "yelp")
    q = request.args.get("q", "")
    if source == "yelp":
        term, location = (q.split(",",1)[0].strip(), q.split(",",1)[1].strip()) if "," in q else (q, "")
        reviews = yelp_reviews_for(term, location)
    else:
        reviews = google_reviews_for(q)
    reviews = analyze_sentiment(reviews)
    summary = weekly_sentiment_summary(reviews)
    return jsonify(summary)

@app.route("/api/competitors")
def get_competitors():
    # You should implement competitor discovery (e.g., search nearby businesses and return top N)
    # For simplicity, we return static or could call Yelp search to find businesses in same category.
    return jsonify([
        {"name": "Business A", "rating": 4.5},
        {"name": "Business B", "rating": 4.0},
        {"name": "Your Business", "rating": 4.2},
    ])

if __name__ == "__main__":
    app.run(debug=True)
