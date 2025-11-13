from celery_app import celery
from scraper_yelp import reviews_for as yelp_reviews_for
from scraper_google import reviews_for as google_reviews_for
from sentiment import analyze_sentiment, extract_entities, weekly_sentiment_summary
from email_sender import send_email_report
import os

@celery.task(name="tasks.send_weekly_report")  # 👈 this name must match celery_app.py schedule
def send_weekly_report():
    monitored = [
        {"source": "yelp", "query": ("coffee shop", "Austin, TX")},
        {"source": "google", "query": "Best Tacos Austin TX"},
    ]
    all_reviews = []
    for m in monitored:
        try:
            if m["source"] == "yelp":
                reviews = yelp_reviews_for(*m["query"])
            else:
                reviews = google_reviews_for(m["query"])
            reviews = analyze_sentiment(reviews)
            reviews = extract_entities(reviews)
            all_reviews.extend(reviews)
        except Exception as e:
            print("fetch error", e)

    summary = weekly_sentiment_summary(all_reviews)
    html = f"<h1>Weekly Report</h1><p>Average sentiment: {summary['average_sentiment']:.3f} over {summary['n_reviews']} reviews</p>"
    send_email_report(subject="Weekly Local Insight Report", html_body=html)
    return {"status": "sent", "n_reviews": summary["n_reviews"]}
