def add_to_order(order, item_name, quantity, price_per_item):
    if not isinstance(quantity, int) or quantity <= 0:
        return False
    if not isinstance(price_per_item, (int, float)) or price_per_item <= 0:
        return False
    
    order[item_name] = {
        'quantity': quantity,
        'price_per_item': price_per_item
    }
    return True

def remove_from_order(order, item_name):
    if item_name in order:
        del order[item_name]
        return True
    return False

def calculate_bill(order, tax_rate):
    subtotal = 0
    for item_data in order.values():
        subtotal += item_data['quantity'] * item_data['price_per_item']
    
    return subtotal + (subtotal * tax_rate / 100)

def get_most_expensive_item(order):
    if not order:
        return None
    
    most_expensive = None
    highest_cost = -1
    
    for item_name, item_data in order.items():
        total_cost = item_data['quantity'] * item_data['price_per_item']
        if total_cost > highest_cost:
            highest_cost = total_cost
            most_expensive = item_name
    
    return most_expensive

# Test
if __name__ == "__main__":
    order = {}

    print(add_to_order(order, "Burger", 2, 8.99))
    print(add_to_order(order, "Fries", -1, 3.50))
    print(add_to_order(order, "Drink", 2, 2.99))

    print(f"Order: {order}")

    total = calculate_bill(order, 10)
    print(f"Total with 10% tax: ${total:.2f}")

    expensive = get_most_expensive_item(order)
    print(f"Most expensive item: {expensive}")

    print(remove_from_order(order, "Drink"))
    print(remove_from_order(order, "Pizza"))