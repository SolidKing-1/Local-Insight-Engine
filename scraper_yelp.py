import requests, os

YELP_API_KEY = os.getenv("YELP_API_KEY")

def reviews_for(term, location):
    if not YELP_API_KEY:
        raise ValueError("Missing Yelp API key. Set YELP_API_KEY in your .env")

    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {"term": term, "location": location, "limit": 1}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    # pick the first business
    business_id = data["businesses"][0]["id"]
    reviews_url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"
    rev_resp = requests.get(reviews_url, headers=headers)
    rev_resp.raise_for_status()
    return rev_resp.json().get("reviews", [])
