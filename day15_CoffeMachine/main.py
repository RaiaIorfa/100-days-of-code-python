MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

def display_status(stock):
    """Print out a formatted status of current stock/resources available in the resources dictionary"""
    for key, value in stock.items():
        if key == "coffee":
            print(f"{key.title()}: {value}g")
        elif key == "money":
            print(f"{key.title()}: ${value}")
        else:
            print(f"{key.title()}: {value}ml")

def check_stock(stock, drink, menu=MENU):
    """Checks resources and returns True if it's enough to prepare the coffee otherwise returns False"""
    ingredients = menu[drink]["ingredients"]
    for ingredient, value in ingredients.items():
        if stock[ingredient] < value:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins:")
    pennies = float(input("How many pennies? "))
    nickels = float(input("How many nickels? "))
    dimes = float(input("How many dimes? "))
    quarters = float(input("How many quarters? "))

    coins = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
    }
    pennies *= coins["penny"]
    nickels *= coins["nickel"]
    dimes *= coins["dime"]
    quarters *= coins["quarter"]
    total = pennies + nickels + dimes + quarters
    return round(total, 2)

def calculate_price(customer_purchase, item, menu=MENU):
    """Checks if the customer money is enough to make the purchase then give out coffee and returns the price of the coffee it True"""
    if customer_purchase > menu[item]["cost"]:
        # TODO: 1. prepare coffee and return the change
        print(f"Here is your {item} ☕ Enjoy!")
        print(f"Here is ${round(customer_purchase - menu[item]["cost"], 2)} in change.")
        return menu[item]["cost"]
    elif customer_purchase < menu[item]["cost"]:
        # TODO: 2. refund the money and print the money is not enough to make the purchase
        print(f"Your money is not enough to purchase a {item}")
        print(f"Here is  your refund ${customer_purchase}")
        return
    elif customer_purchase == menu[item]["cost"]:
        # TODO: 3. prepare the coffee
        print(f"Here is your {item} ☕ Enjoy!")
        return menu[item]["cost"]

def update_resources(stock, item, price, menu=MENU):
    new_resources = stock

    ingredients = menu[item]["ingredients"]
    for ingredient, value in ingredients.items():
        new_resources[ingredient] = stock[ingredient] - value
    new_resources["money"] += price
    return new_resources

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
power = True

while power:
    print("_" * 100)
    option = input("What would you like? \n🍵 Espresso\n🍵 Latte\n🍵 Cappuccino\n\n").lower()
    print("_" * 100 + "\n") 

    if option == "report":
        display_status(resources)
    elif option == "off":
        power = False
        print("Shutting Down.....")
    elif option == "espresso":
        if check_stock(resources, option):
            purchase = process_coins()
            price = calculate_price(purchase, option)
            if price:
                resources = update_resources(resources, option, price)
    elif option == "latte":
        if check_stock(resources, option):
            purchase = process_coins()
            price = calculate_price(purchase, option)
            if price:
                resources = update_resources(resources, option, price)
    elif option == "cappuccino":
        if check_stock(resources, option):
            purchase = process_coins()
            price = calculate_price(purchase, option)
            if price:
                resources = update_resources(resources, option, price)            