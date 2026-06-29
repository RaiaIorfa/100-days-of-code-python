import tkinter as tk

screen = tk.Tk()
screen.minsize(width=500, height=500)
screen.title("My First GUI")

my_label = tk.Label(text="New Text")
my_label['font'] = ("Times New Roman", 16, "bold")
my_label.pack()

def change_text():
    my_label["text"] = input.get()

button = tk.Button(text="Click me", command=change_text)
button.pack()

input = tk.Entry(width=12)
input.pack()
print(input.get())










screen.mainloop()