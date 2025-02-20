import json

ACCOUNTS_FILE = "accounts.json"

def load_accounts():
    try:
        with open(ACCOUNTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(accounts, file)

def add_account(username, password):
    accounts = load_accounts()
    accounts[username] = password
    save_accounts(accounts)
    return f"✅ Account {username} added successfully!"

def switch_account(username):
    accounts = load_accounts()
    if username in accounts:
        return f"✅ Switched to {username}."
    return "❌ Account not found!"
