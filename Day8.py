# # **Task 1:**
# # Create a class called BankAccount with:
# # - attributes: owner, balance
# # - methods: 
# #     deposit(amount) — adds to balance
# #     withdraw(amount) — subtracts, but print "Insufficient funds" if balance < amount
# #     display() — prints owner name and current balance
# # Create 2 accounts and test all methods.

class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance 
        else:
            print("Insufficient Funds")   

    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

c1 = BankAccount("Khushi", 56499)              
c2 = BankAccount("Nishu", 415136)

c1.deposit(468)
c2.withdraw(454468)

c1.display()
c2.display()

# **Task 2:**
# Create a class called Book with:
# - attributes: title, author, pages
# - method: summary() — prints all details in one clean line

# Create a list of 3 Book objects.
# Print summary of books with more than 300 pages.

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author =author
        self.pages =pages
         

    def summary(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

Booklist = [
    Book("The house is not a home", "John doe", 733),
    Book("Rich dad poor dad", "joms bolt", 332,),
    Book("power of compunding", "xyz", 234)]

for book in Booklist:
    if Book.pages >300:
        Book.summary() 
