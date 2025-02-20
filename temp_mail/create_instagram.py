import requests

def create_new_account():
    email = requests.get("https://temp-mail-api.com").json()["email"]
    password = "TempPass123!"
    
    signup_data = {
        "email": email,
        "password": password,
        "username": "insta_user_" + email.split('@')[0],
        "full_name": "New Instagram User"
    }

    response = requests.post("https://www.instagram.com/accounts/web_create_ajax/", data=signup_data)
    
    if response.status_code == 200:
        return f"✅ Instagram Account Created: {signup_data['username']}"
    else:
        return "❌ Failed to Create Account!"
