# Open the starting letter file
with open("./Input/Letters/starting_letter.txt") as data:
    starting_letter = data.read()

print(starting_letter)

# Get each name in invited_names.txt and store in a list
with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
    invited_names = [] 
    for name in names:
        strip = name.strip("\n")
        invited_names.append(strip)

print(invited_names)

# For each name in invited_names create a letter using the starting_letter and save it in ReadyToSend Folder
for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as letter:
        letter.write(starting_letter.replace("[name]", name))
