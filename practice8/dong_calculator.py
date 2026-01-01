import tkinter as tk
from tkinter import messagebox


def calculate_bill():
    try:
        total_bill = float(entry_total_bill.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid total bill")
        return
    try:
        number_of_people = int(entry_number_of_people.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of people")
        return
    if number_of_people == 0:
        messagebox.showerror("Error", "Number of people cannot be zero")
        return
    amount_per_person = total_bill / number_of_people
    messagebox.showinfo("Amount per Person", f"Each person should pay: ${amount_per_person}")



root = tk.Tk()

root.title("Register")
root.geometry("400x300")

# 3 main widgets ( Label, Entry, Button )
# row 0 column 0 username label widget
label_total_bill = tk.Label(root, text="Total Bill")
label_total_bill.grid(row=0, column=0, padx=10, pady=10)

# row 0 column 1 username entry widget
entry_total_bill = tk.Entry(root)
entry_total_bill.grid(row=0, column=1, padx=10, pady=10)

# row 1 column 0 password label widget
label_number_of_people = tk.Label(root, text="Number of People")
label_number_of_people.grid(row=1, column=0, padx=10, pady=10)

# row 1 column 1 password entry widget
entry_number_of_people = tk.Entry(root)
entry_number_of_people.grid(row=1, column=1, padx=10, pady=10)

# row 2 column 0 with taking two columns space login button widget
button_login = tk.Button(root, text="Login", command=calculate_bill)
button_login.grid(row=2, column=0, columnspan=2, pady=20)


root.mainloop()
print("This line will be printed after the program closes.")





# Dong Calculator

