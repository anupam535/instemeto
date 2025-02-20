import os
import telebot
from automation.instagram import instagram_login, watch_reels, ai_comment_on_reel
from automation.database import get_accounts, add_account
from automation.proxy import get_proxy


# ✅ Direct Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7604424348:AAHtkmD0YKApTg4B9-QeJNW5SXUmOmctK7E"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! AI Instagram Automation Activated.")

bot.polling()

@bot.message_handler(commands=['watch_reels'])
def watch_reels_command(message):
    """Watches Instagram reels from all added accounts."""
    try:
        reels_url = message.text.split(" ")[1]
        accounts = get_accounts()

        if not accounts:
            bot.reply_to(message, "❌ No Instagram accounts found! Use /add_account first.")
            return

        for username, password in accounts:
            proxy = get_proxy()
            driver = instagram_login(username, password, proxy)
            watch_reels(driver, reels_url)
            driver.quit()

        bot.reply_to(message, f"✅ Watched reels at {reels_url} from all accounts!")
    except IndexError:
        bot.reply_to(message, "❌ Use: /watch_reels <reels_url>")

@bot.message_handler(commands=['ai_comment'])
def ai_comment_command(message):
    """Posts AI-generated comments on a reel."""
    try:
        reels_url = message.text.split(" ")[1]
        accounts = get_accounts()

        if not accounts:
            bot.reply_to(message, "❌ No accounts found! Add one using /add_account.")
            return

        for username, password in accounts:
            proxy = get_proxy()
            driver = instagram_login(username, password, proxy)
            ai_comment_on_reel(driver, reels_url)
            driver.quit()

        bot.reply_to(message, f"✅ AI-commented on reel {reels_url} from all accounts!")
    except IndexError:
        bot.reply_to(message, "❌ Use: /ai_comment <reels_url>")

bot.polling()
