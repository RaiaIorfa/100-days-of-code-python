student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(value)
    # print(key)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(row.student)
    #Access row.student/row["student"] or row.score/row["score"]
    pass

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)

# Keyword Method with iterrows()
phonetic_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

