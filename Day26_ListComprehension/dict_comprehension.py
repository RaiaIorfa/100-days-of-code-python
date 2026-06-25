# -------------------DICTIONARY COMPREHENSION-------------------
# --------SYNTAX--------
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if condition }

import random
names = ["Alex", "Caroline", "Dave", "Elanor", "Freddie"]
student_scores = {name:random.randint(1,100) for name in names}
print(student_scores)

passed_students = {key:value for (key,value) in student_scores.items() if value >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word) for word in words}
print(result)
