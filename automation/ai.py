import openai
import random

# ✅ Direct OpenAI API Key
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def generate_ai_caption(topic):
    """AI se ek engaging Instagram caption generate karega."""
    prompt = f"Generate an engaging Instagram caption about {topic}."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    
    return response["choices"][0]["text"].strip()


def generate_ai_comment():
    """AI se ek natural aur engaging Instagram comment generate karta hai."""
    openai.api_key = OPENAI_API_KEY
    responses = [
        "That's amazing! 🔥🔥",
        "This is so cool! 😍",
        "Absolutely love this! 💯",
        "Insane content! Keep going! 🚀",
        "Wow, this is next level! 🤯",
        "Superb work! Keep shining! ✨"
    ]
    return random.choice(responses)

def generate_ai_caption(topic):
    """AI se ek engaging Instagram caption generate karta hai."""
    openai.api_key = OPENAI_API_KEY
    prompt = f"Create a catchy Instagram caption about {topic} in a cool and engaging style."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response["choices"][0]["text"].strip()

def generate_ai_hashtags(topic):
    """AI se trending Instagram hashtags generate karta hai."""
    openai.api_key = OPENAI_API_KEY
    prompt = f"Generate 10 trending Instagram hashtags related to {topic}."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    
    hashtags = response["choices"][0]["text"].strip()
    return hashtags.replace("\n", " ")  # Saare hashtags ek line me aa jayenge

# Testing (Direct Run)
if __name__ == "__main__":
    print("AI Comment:", generate_ai_comment())
    print("AI Caption:", generate_ai_caption("adventure travel"))
    print("AI Hashtags:", generate_ai_hashtags("fitness motivation"))
