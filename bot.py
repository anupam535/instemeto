import telebot
from automation import (
    auto_likes, auto_comments, auto_followers, auto_reels, auto_dm, trend_detection,
    proxy_manager, account_manager
)
from temp_mail import create_instagram

# ✅ Telegram Bot API Token
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# ✅ Command: Start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Instagram Automation Activated! Use /help to see commands.")

# ✅ Command: Help (Shows all available commands)
@bot.message_handler(commands=['help'])
def show_help(message):
    commands = """
    🔹 /boost_likes <post_url> <count> - Mass Auto-Like Posts
    🔹 /boost_comments <post_url> <count> - AI Smart Commenting
    🔹 /boost_followers <count> - Auto-Follower Growth
    🔹 /watch_reels <username> - Auto-Watch Reels
    🔹 /watch_stories <username> - Auto-Watch Stories
    🔹 /set_proxy <proxy_url> - Add Proxy
    🔹 /enable_auto_proxy - Enable Auto Proxy Rotation
    🔹 /create_account - Auto Create Instagram Account
    🔹 /switch_account <account_id> - Switch Between Accounts
    🔹 /trend_detect - Detect Viral Instagram Trends
    """
    bot.reply_to(message, commands)

# ✅ Command: Boost Likes
@bot.message_handler(commands=['boost_likes'])
def boost_likes(message):
    try:
        _, post_url, count = message.text.split()
        response = auto_likes.mass_like(post_url, int(count))
        bot.reply_to(message, f"✅ {response} Likes added!")
    except:
        bot.reply_to(message, "❌ Invalid Command! Use: /boost_likes <post_url> <count>")

# ✅ Command: Boost Comments
@bot.message_handler(commands=['boost_comments'])
def boost_comments(message):
    try:
        _, post_url, count = message.text.split()
        response = auto_comments.smart_comment(post_url, int(count))
        bot.reply_to(message, f"✅ {response} Comments added!")
    except:
        bot.reply_to(message, "❌ Invalid Command! Use: /boost_comments <post_url> <count>")

# ✅ Command: Create Instagram Account
@bot.message_handler(commands=['create_account'])
def create_account(message):
    response = create_instagram.create_new_account()
    bot.reply_to(message, response)

bot.polling()
