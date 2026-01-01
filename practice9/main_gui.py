import logic
import tkinter as tk
from tkinter import messagebox

# listbox widget to show contacts
# listbox.insert(tk.END, "text")
#listbox.delete(0, tk.END)

book = logic.PhoneBook()

def refresh_contacts_list():
    listbox_contacts.delete(0, tk.END)
    for contact in book.contacts:
        display_text = f"{contact.name}: {contact.phone_number}"
        listbox_contacts.insert(tk.END, display_text)
        
def button_add_contact_clicked():
    name = entry_name.get()
    phone_number = entry_phone.get()
    if not name or not phone_number:
        messagebox.showerror("Error", "Please enter both name and phone number")
        return
    try:
        book.add_contact(name, phone_number)
        refresh_contacts_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        
def button_save_contacts_clicked():
    book.save_to_csv("contacts.csv")
    messagebox.showinfo("Success", "Contacts saved to contacts.csv")
    
def button_load_contacts_clicked():
    book.load_from_csv("contacts.csv")
    refresh_contacts_list()
    
    messagebox.showinfo("Success", "Contacts loaded from contacts.csv")
    
def button_search_contact_clicked():
    search_term = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in book.contacts:
        if search_term in contact.name.lower() or search_term in contact.phone_number:
            display_text = f"{contact.name}: {contact.phone_number}"
            listbox_contacts.insert(tk.END, display_text)
            
def button_exit_clicked():
    try:
        book.save_to_csv("contacts.csv")
        messagebox.showinfo("Exit", "Contacts saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save contacts:\n{e}")
        return

    root.destroy()
    
    
root = tk.Tk()
root.title("Phone Book")
root.geometry("500x500")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(top_frame)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Phone Number").grid(row=1, column=0)
entry_phone = tk.Entry(top_frame)
entry_phone.grid(row=1, column=1, padx=5)

mid_frame = tk.Frame(root)
mid_frame.pack(pady=10)
tk.Label(mid_frame, text="Search").grid(row=0, column=0)
entry_search = tk.Entry(mid_frame)
entry_search.grid(row=0, column=1, padx=5)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Search Contact", command=button_search_contact_clicked).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Add Contact", command=button_add_contact_clicked).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Save Contacts", command=button_save_contacts_clicked).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Load Contacts", command=button_load_contacts_clicked).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Exit", command=button_exit_clicked).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Contacts List: ").pack(pady=(20, 0))
listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.pack(pady=5)
tk.Label(root, text="when loading, duplicated contacts are skipped").pack(pady=(20, 0))

root.mainloop()
