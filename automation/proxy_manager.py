import requests

PROXY_LIST_URL = "https://www.proxy-list.download/api/v1/get?type=https"

def fetch_proxies():
    response = requests.get(PROXY_LIST_URL)
    if response.status_code == 200:
        proxies = response.text.split("\n")
        return proxies
    return []

def rotate_proxy():
    proxies = fetch_proxies()
    if proxies:
        current_proxy = proxies[0]
        return f"✅ Proxy set to {current_proxy}"
    return "❌ No proxies available!"
