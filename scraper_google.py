# backend/scraper_google.py
import os, requests
from typing import List, Dict

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

def get_place_id_by_text(query: str) -> str:
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": query, "key": GOOGLE_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()
    if data.get("results"):
        return data["results"][0]["place_id"]
    return ""

def get_place_reviews(place_id: str) -> List[Dict]:
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {"place_id": place_id, "fields": "name,rating,review", "key": GOOGLE_KEY}
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()
    result = data.get("result", {})
    reviews = []
    for item in result.get("reviews", []):
        reviews.append({
            "username": item.get("author_name"),
            "rating": item.get("rating"),
            "comment": item.get("text"),
            "time_created": item.get("time"),
            "source": "google",
            "review_id": item.get("review_id", None),
        })
    return reviews

def reviews_for(query: str):
    pid = get_place_id_by_text(query)
    return get_place_reviews(pid)

def search_places(query: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": query, "key": GOOGLE_KEY}

    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()

    results = []
    for p in data.get("results", []):
        results.append({
            "name": p.get("name"),
            "rating": p.get("rating"),
            "address": p.get("formatted_address"),
            "place_id": p.get("place_id"),
        })
    return results
