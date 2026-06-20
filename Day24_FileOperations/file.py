# ----You won't need to worry about closing the file 'with' keyword handles it automatically------
with open("my_file.txt") as open_file:
    content = open_file.read()
    print(content)

# ----The defualt mode is read only. If you need to write into the file set mode='w' write_mode ------
with open("my_file.txt", mode="w") as open_file:
    open_file.write("Hello world")
    # content = open_file.read()
    # print(content)

# ----If you need to append into the file without deleting previous contents set mode='a' append_mode ------
with open("my_file.txt", mode="a") as open_file:
    open_file.write("\nHello World.")
    # content = open_file.read()
    # print(content)


# ------Using this method will require you to manually close the file at the end of your operations-------
# open_file = open("my_file.txt", mode="w")
# content = open_file.read()
# print(content)
# open_file.close()