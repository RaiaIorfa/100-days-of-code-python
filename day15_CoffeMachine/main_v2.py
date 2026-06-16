# --------------Gemini Code Tutor-----------------
# ---------------CLEANER VERSION------------------
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

def display_status(stock):
    """Print out a formatted status of current stock/resources available."""
    for key, value in stock.items():
        if key == "coffee":
            print(f"{key.title()}: {value}g")
        elif key == "money":
            print(f"{key.title()}: ${value:.2f}")
        else:
            print(f"{key.title()}: {value}ml")

def check_stock(stock, drink):
    """Checks resources and returns True if ingredients are sufficient, otherwise False."""
    ingredients = MENU[drink]["ingredients"]
    for ingredient, value in ingredients.items():
        if stock[ingredient] < value:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    """Prompts user for coins and returns the total value calculated."""
    print("Please insert coins:")
    try:
        total = int(input("How many pennies? ")) * 0.01
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many dimes? ")) * 0.10
        total += int(input("How many quarters? ")) * 0.25
        return round(total, 2)
    except ValueError:
        print("Invalid coin input. Transaction aborted.")
        return 0

def handle_transaction(customer_purchase, item):
    """Evaluates money given, provides change/refund, and returns the item cost if successful."""
    cost = MENU[item]["cost"]
    if customer_purchase >= cost:
        change = round(customer_purchase - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {item} ☕ Enjoy!")
        return cost
    else:
        print(f"Your money is not enough to purchase a {item}. Here is your refund: ${customer_purchase}")
        return 0

def update_resources(stock, item, price):
    """Deducts ingredients from stock and adds transaction revenue in-place."""
    ingredients = MENU[item]["ingredients"]
    for ingredient, value in ingredients.items():
        stock[ingredient] -= value
    stock["money"] += price

# --- MAIN EXECUTION MACHINE ---
if __name__ == "__main__":
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
    power = True

    while power:
        print("_" * 50)
        option = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
        print("_" * 50 + "\n") 

        if option == "off":
            power = False
            print("Shutting Down.....")
        elif option == "report":
            display_status(resources)
        elif option in MENU:  # FIXED: Handles ALL current and future menu items dynamically!
            if check_stock(resources, option):
                purchase = process_coins()
                price_paid = handle_transaction(purchase, option)
                if price_paid > 0:
                    update_resources(resources, option, price_paid)  # Mutates resources cleanly
        else:
            print("❌ Invalid selection. Please choose an item from our menu.")