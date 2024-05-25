# Author: Dhaval Patel. Codebasics YouTube Channel

import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)
        return extracted_string

    return ""


def generate_order_string(item_quantities, item_prices):
    order_items = []
    total_cost = 0
    for item, quantity in item_quantities.items():
        if item in item_prices:
            price = item_prices[item]
            total_cost += quantity * item_prices[item]
            order_items.append(f"{quantity} {item} price ${price} each")
        else:
            order_items.append(f"{quantity} {item} price not available")
    return ", ".join(order_items), total_cost


def convert_keys_to_lowercase(dictionary):
    return {key.lower(): value for key, value in dictionary.items()}



if __name__ == "__main__":
    # Example usage
    item_quantities = {"pizza": 2, "samosa": 1}
    item_prices = {"pizza": 8, "samosa": 9}
    order_string = generate_order_string(item_quantities, item_prices)
    print(order_string)

  

