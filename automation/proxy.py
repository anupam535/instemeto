import requests

def get_proxy():
    """Fetches a working proxy from a proxy provider."""
    response = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http")
    proxies = response.text.split("\n")
    return proxies[0] if proxies else None
