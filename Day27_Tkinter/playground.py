import customtkinter as ctk

window  = ctk.CTk()
window.minsize(width=500, height=500)
window.title("My GUI")
window.config(padx=20, pady=20)
font = ("Times New Roman", 16, "bold")

my_label =  ctk.CTkLabel(window, text="New Label", font=font)
my_label.grid(column=0, row=0)

button1 = ctk.CTkButton(window, text="Button1")
button1.grid(column=1, row=2)

button2 =  ctk.CTkButton(window, text="Button2")
button2.grid(column=2, row=0)

input_field = ctk.CTkEntry(window)
input_field.grid(column=3, row=3)







window.mainloop()