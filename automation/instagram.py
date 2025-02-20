from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import openai

# OpenAI API Key for AI-generated comments
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

def generate_ai_comment():
    """Generates a unique AI-powered comment."""
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate a natural and engaging Instagram comment.",
        max_tokens=20
    )
    return response["choices"][0]["text"].strip()

def instagram_login(username, password, proxy=None):
    """Logs into Instagram with the given credentials and optional proxy."""
    options = webdriver.ChromeOptions()
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(random.uniform(5, 7))

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").submit()
    time.sleep(random.uniform(5, 7))

    return driver

def watch_reels(driver, reels_url):
    """Watches multiple reels for engagement boost."""
    driver.get(reels_url)
    time.sleep(random.uniform(5, 7))

    try:
        while True:
            next_button = driver.find_element(By.XPATH, "//button[contains(@class, 'coreSpriteRightChevron')]")
            next_button.click()
            time.sleep(random.uniform(10, 15))  # Watches each reel for at least 10 seconds
    except:
        print("✅ Finished watching all reels.")

def ai_comment_on_reel(driver, reels_url):
    """Generates an AI-based comment and posts it on the reel."""
    driver.get(reels_url)
    time.sleep(random.uniform(3, 5))

    comment = generate_ai_comment()
    
    comment_box = driver.find_element(By.XPATH, "//textarea[contains(@class, 'comment')]")
    comment_box.send_keys(comment)
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
    submit_button.click()
    time.sleep(3)
