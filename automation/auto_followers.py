from instagrapi import Client

def auto_follow(username, count):
    cl = Client()
    cl.login("username", "password")

    user_id = cl.user_id_from_username(username)
    for _ in range(count):
        cl.user_follow(user_id)

    return f"✅ {count} followers added to {username}."
