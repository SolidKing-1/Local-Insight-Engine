import requests
from bs4 import BeautifulSoup

def scrape_yelp_reviews(business_url: str, limit: int = 10):
    """
    Scrape reviews from a Yelp business page using requests + BeautifulSoup.
    Example: business_url = "https://www.yelp.com/biz/mcdonalds-new-york"
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(business_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch Yelp page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    reviews = []

    for review in soup.select("div.review__373c0__13kpL")[:limit]:
        username = review.select_one("span.fs-block").get_text(strip=True) if review.select_one("span.fs-block") else "Anonymous"
        comment = review.select_one("p.comment__373c0__1M-px").get_text(strip=True) if review.select_one("p.comment__373c0__1M-px") else ""
        rating_tag = review.select_one("div.i-stars__373c0__1T6rz")
        rating = float(rating_tag["aria-label"].split()[0]) if rating_tag and "aria-label" in rating_tag.attrs else None

        reviews.append({
            "username": username,
            "rating": rating or 0,
            "comment": comment
        })

    return reviews
