from instagrapi import Client
import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def generate_comment(topic):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a creative Instagram comment about {topic}.",
        max_tokens=30
    )
    return response["choices"][0]["text"].strip()

def smart_comment(post_url, count):
    cl = Client()
    cl.login("username", "password")
    
    media_id = cl.media_id(post_url)
    for _ in range(count):
        comment_text = generate_comment("Instagram engagement")
        cl.media_comment(media_id, comment_text)

    return count
