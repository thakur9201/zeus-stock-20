import json
from telegram_bot import send_message

with open("products.json", "r") as f:
    products = json.load(f)

for product in products:
    in_stock = product.get("stock", False)
    
    if in_stock:
        send_message(
            f"🔥 Stock Alert!\n\n"
            f"📦 {product['name']}\n"
            f"🔗 {product['url']}"
        )
