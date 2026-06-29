import customtkinter as ctk

def miles_to_km():
    km = 1.61
    miles = float(miles_input.get())
    result = round(miles * km, 2)
    km_unit_label.configure(text=f"{result:.2f}")

root  = ctk.CTk()
# root.geometry("300x300")
root.title("Unit Converter")
root.config(padx=30, pady=100)

miles_input = ctk.CTkEntry(root)
miles_input.grid(row=0, column=1)

miles_label = ctk.CTkLabel(root, text=" Miles")
miles_label.grid(row=0, column=2)

equalto_label = ctk.CTkLabel(root, text="is equal to")
equalto_label.grid(row=1, column=0)

km_unit_label = ctk.CTkLabel(root, text="0") 
km_unit_label.grid(row=1, column=1)

km_label = ctk.CTkLabel(root, text="Km")
km_label.grid(row=1, column=2)

calculate = ctk.CTkButton(root, text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)















root.mainloop()