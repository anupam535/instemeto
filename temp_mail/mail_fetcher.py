import requests

TEMP_MAIL_API = "https://temp-mail-api.com/api/v1/inbox"

def fetch_otp(email):
    response = requests.get(f"{TEMP_MAIL_API}?email={email}")
    if response.status_code == 200:
        emails = response.json()
        for mail in emails:
            if "verification code" in mail["subject"].lower():
                return mail["text"]
    return "❌ No verification email found!"
