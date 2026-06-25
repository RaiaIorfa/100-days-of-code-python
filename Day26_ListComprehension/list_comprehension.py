# -------------------LIST COMPREHENSION-------------------
# --------SYNTAX--------
# new_list = [{logic/expression for new_item value} for {item} in {list/anysequence}]

numbers = [1, 2, 3, 4, 5]

new_list = [num + 1 for num in numbers]

print(new_list)
print(numbers)
print("\n")
print("-" * 50)

double_num = [num * 2 for num in range(1, 5)]
print(double_num)

print("\n")
print("-" * 50)

# list comprehension with condition
# --------SYNTAX--------
# new_list = [{logic/expression for new_item value} for {item} in {list/anysequence} if {condition}]
names = ["Alex", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name for name in names if len(name) > 4]
print(long_names)
upper_long_names = [name.upper() for name in names if len(name) > 4]
print(upper_long_names)