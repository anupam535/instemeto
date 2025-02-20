import requests

def detect_instagram_trends():
    response = requests.get("https://www.instagram.com/explore/tags/trending/")  
    if response.status_code == 200:
        return "✅ Fetched trending Instagram hashtags!"
    return "❌ Failed to detect trends."
