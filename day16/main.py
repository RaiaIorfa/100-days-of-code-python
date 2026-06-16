from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

power = True
while power:
    print("_" * 100)
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    print("_" * 100 + "\n")
    if choice == "off":
        power = False
        print("Shuting Down...........")
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffe_maker.make_coffee(item)
