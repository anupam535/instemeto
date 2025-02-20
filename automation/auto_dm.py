from instagrapi import Client
import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def generate_reply(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a professional response to this Instagram DM: {message}",
        max_tokens=50
    )
    return response["choices"][0]["text"].strip()

def auto_dm_reply():
    cl = Client()
    cl.login("username", "password")

    inbox = cl.direct_threads()
    for thread in inbox:
        messages = cl.direct_messages(thread.id)
        last_message = messages[0].text  

        if not messages[0].seen:
            reply = generate_reply(last_message)
            cl.direct_send(reply, thread.id)

    return "✅ Auto-replies sent to unread DMs!"
