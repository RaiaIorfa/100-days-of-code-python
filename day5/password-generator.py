import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Setting the variables
password = ""
shuffle_password =""
password_lists = []

# Generating random sequence of characters

for i in range(0, nr_letters):
    password += random.choice(letters)

for i in range(0, nr_numbers):
    password += random.choice(numbers)

for i in range(0, nr_symbols):
    password += random.choice(symbols)
    
print(f"Your password is: {password}")

# Moving the generated password into a list

for i in range(0, len(password)):
    password_lists.append(password[i])

# Shuffle the list

print(password_lists)
random.shuffle(password_lists)
print(password_lists)

# print password

for char in password_lists:
    shuffle_password += char 

print(f"Your password is: {shuffle_password}")