from instagrapi import Client

def auto_watch_reels(username):
    cl = Client()
    cl.login("username", "password")

    user_id = cl.user_id_from_username(username)
    reels = cl.user_medias(user_id, amount=10)  

    for reel in reels:
        cl.media_view(reel.pk)  

    return f"✅ Watched {len(reels)} reels of {username}."

def auto_watch_stories(username):
    cl = Client()
    cl.login("username", "password")

    user_id = cl.user_id_from_username(username)
    stories = cl.user_stories(user_id)

    for story in stories:
        cl.media_view(story.pk)

    return f"✅ Watched {len(stories)} stories of {username}."
