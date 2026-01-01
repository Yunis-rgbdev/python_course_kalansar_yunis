#logic.py
import csv

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits.")
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
            with open(file, "w", newline="", encoding="utf-8") as f:
                 writer = csv.writer(f)
                 writer.writerow(["Name", "Phone Number"])
                 for contact in self.contacts:
                     writer.writerow([contact.name, contact.phone_number])
            print(f"Successfully saved {len(self.contacts)} contacts to {file}")
        except PermissionError:
            print(f"Error: Permission denied when trying to write to {file}.")
            
    def load_from_csv(self, file):
        try:
            with open(file, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    try:
                        name = row[0]
                        phone_number = row[1]

                        
                        duplicate = False
                        for contact in self.contacts:
                            if contact.name == name and contact.phone_number == phone_number:
                                duplicate = True
                                break

                        if duplicate:
                            print(f"Duplicate contact skipped: {name}, {phone_number}")
                            continue

                        self.add_contact(name, phone_number)

                    except ValueError as e:
                        print(f"Invalid contact skipped {row}: {e}")
                    except IndexError:
                        print(f"Corrupted row skipped: {row}")

                print(f"Loaded contacts. Total: {len(self.contacts)}")

        except FileNotFoundError:
            print(f"File '{file}' not found. New phonebook created.")
            
        