import csv

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits.")
        
        if len(phone_number) < 11 or len(phone_number) > 11:
            raise ValueError("Phone number must be exactly 11 digits long.")
        self.phone_number = phone_number
        
        
class PhoneBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, name, phone_number):
        try:
            contact = Contact(name, phone_number)
            self.contacts.append(contact)
        except ValueError as e:
            print(f"Error adding contact: {e}")
            
    def save_to_csv(self, file):
        try:
            with open(file, "w", newline="", encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Phone Number"])
                for contacts in self.contacts:
                    writer.writerow([contacts.name, contacts.phone_number])
                print(f"successfully saved {len(self.contacts)} to {file}")
        except FileNotFoundError:
            print(f"Error: The file {file} was not found. Creating a new file.")        
        
    def load_from_csv(self, file):
        try:
            with open(file, "r", newline="", encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    try:
                        name = row[0]
                        phone = row[1]
                        print( f"Loading contact: {name}, {phone}")
                        self.add_contact(name, phone)
                    except IndexError:
                        print(f"Error: corrupted row in csv file, skipping row {row}")
                        
                print(f"loaded list of contacts from csv file\n {len(self.contacts)} contacts loaded.")
        except FileNotFoundError:
            print(f"Error: The file {file} was not  found.")
            
            
            
            
#main program
phonebook = PhoneBook()
while True:
    try:
        choice = input("Choose an action:\n1. Add Contact\n2. Save Contacts to csv\n3. Load Contacts from csv\n4. Exit\n")
        
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 4:
            print("Please enter a digit from 1-4")
            continue
        
        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            try:
                phonebook.add_contact(name, phone)
            except ValueError as e:
                print(f"Wrong number format: {e}")
        elif choice == "2":
            filename = input("Enter filename to save contacts: (default: contacts.csv)")
            if filename.strip() == "":
                filename = "contacts.csv"
            phonebook.save_to_csv(filename)
        elif choice == "3":
            filename = input("Enter filename to load contacts from: (default: contacts.csv)")
            if filename.strip() == "":
                filename = "contacts.csv"
            phonebook.load_from_csv(filename)
        elif choice == "4":
            break
    except ValueError as e:
        print(f"Please Enter a digit 1-4: {e}")          