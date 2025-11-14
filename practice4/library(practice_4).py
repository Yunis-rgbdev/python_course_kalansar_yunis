class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_details(self):
        print(f"Title: { self.title } \n Author: { self.author } \n Price: { self.price }$")
        
    def apply_discount(self, discount):
        self.price = self.price - self.price * int(discount) / 100
        

book_1 = Book("Dont be a frog", "Lewis", 10)
book_2 = Book("Hello Henry", "Sarah", 20)
_discount = input("Enter a discount number from 1 - 100: ")
Book.display_details(book_1)
Book.apply_discount(book_2, _discount)
Book.display_details(book_2)