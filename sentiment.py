import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0.1 else "Negative" if polarity < -0.1 else "Neutral"
    return sentiment, polarity

def extract_entities(text: str):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "SERVICE", "WORK_OF_ART"]]

def analyze_reviews(reviews):
    analyzed = []
    for review in reviews:
        sentiment, polarity = analyze_sentiment(review["comment"])
        entities = extract_entities(review["comment"])
        analyzed.append({
            **review,
            "sentiment": sentiment,
            "polarity": polarity,
            "entities": entities
        })
    return analyzed

def weekly_sentiment_summary(reviews):
    if not reviews:
        return {"average_sentiment": 0, "n_reviews": 0}
    scores = []
    for r in reviews:
        if "polarity" in r:
            scores.append(r["polarity"])
        else:
            _, p = analyze_sentiment(r["comment"])
            scores.append(p)
    avg = sum(scores) / len(scores)
    return {
        "average_sentiment": avg,
        "n_reviews": len(reviews),
        "summary": "Positive" if avg > 0.1 else "Negative" if avg < -0.1 else "Neutral"
    }
