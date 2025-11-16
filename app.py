# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper_yelp import reviews_for as yelp_reviews_for, search_businesses as yelp_search
from scraper_google import reviews_for as google_reviews_for, search_places as google_search
from sentiment import analyze_reviews, weekly_sentiment_summary
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# -------------------------------
# GET REVIEWS (Yelp or Google)
# -------------------------------
@app.route("/api/reviews")
def get_reviews():
    source = request.args.get("source", "yelp")
    q = request.args.get("q", "")

    try:
        if source == "yelp":
            if "," in q:
                term, location = [x.strip() for x in q.split(",", 1)]
            else:
                term, location = q, ""
            reviews = yelp_reviews_for(term, location)

        else:
            reviews = google_reviews_for(q)

        reviews = analyze_reviews(reviews)
        return jsonify(reviews)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# GET WEEKLY SUMMARY
# -------------------------------
@app.route("/api/sentiment-summary")
def get_summary():
    source = request.args.get("source", "yelp")
    q = request.args.get("q", "")

    try:
        if source == "yelp":
            if "," in q:
                term, location = [x.strip() for x in q.split(",", 1)]
            else:
                term, location = q, ""
            reviews = yelp_reviews_for(term, location)
        else:
            reviews = google_reviews_for(q)

        reviews = analyze_reviews(reviews)
        summary = weekly_sentiment_summary(reviews)
        return jsonify(summary)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------------
# COMPETITOR DISCOVERY
# -------------------------------
@app.route("/api/competitors")
def get_competitors():
    source = request.args.get("source", "yelp")
    q = request.args.get("q", "")

    try:
        if source == "yelp":
            if "," in q:
                term, location = [x.strip() for x in q.split(",", 1)]
            else:
                term, location = q, ""
            competitors = yelp_search(term, location)

        else:
            competitors = google_search(q)

        return jsonify(competitors)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
