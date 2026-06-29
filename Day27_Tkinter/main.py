# import tkinter

# window = tkinter.Tk()
# window.title("My GUI program")
# window.minsize(width=500, height=500)


# # -----------------Tkinter components-----------------
# # --------Lables--------
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 16))
# my_label.pack()

# window.mainloop()

def add(*arg):
    sum_n = 0
    for n in arg:
        sum_n += n

    return sum_n

print(add(5,5,5,5,5))