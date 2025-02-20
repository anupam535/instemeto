from automation.proxy_manager import rotate_proxy

def setup_proxy_for_account():
    new_proxy = rotate_proxy()
    return f"✅ Assigned new proxy: {new_proxy}"
