from os import system
from art import logo
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

results_list = []
continue_calc = True
should_continue = True

while continue_calc:
    if should_continue == "y":
        system("cls")
        print(logo[0])
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[operation_symbol](results_list[-1], num2)
        print(f"{results_list[-1]} {operation_symbol} {num2} = {result}")

        results_list.append(result)
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'x' to exit: ").lower()

    elif should_continue == "n" or should_continue == True:
        system("cls")
        print(logo[0])
        num1 = float(input("What's the first number?: "))
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        results_list.append(result)
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'x' to exit: ").lower()
    else: 
        should_continue = False
        continue_calc = False
