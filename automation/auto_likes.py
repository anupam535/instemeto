from instagrapi import Client

def mass_like(post_url, count):
    cl = Client()
    cl.login("username", "password")

    media_id = cl.media_id(post_url)
    for _ in range(count):
        cl.media_like(media_id)
    
    return count
