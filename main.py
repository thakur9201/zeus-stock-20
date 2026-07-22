import json
import time

from telegram_bot import send_message
from config import CHECK_INTERVAL

last_status = {}

while True:
    with open("products.json", "r") as f:
        products = json.load(f)

    for product in products:
        in_stock = product.get("stock", False)

        if in_stock and not last_status.get(product["id"], False):
            send_message(
                f"🔥 Stock Alert!\n\n"
                f"📦 {product['name']}\n"
                f"🔗 {product['url']}"
            )

        last_status[product["id"]] = in_stock

    time.sleep(CHECK_INTERVAL)
