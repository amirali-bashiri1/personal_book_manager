import os
from dotenv import load_dotenv
from books import show_books, save_books, load_books
load_dotenv()
user_name = input("Enter your name: ")
print("Welcome", user_name)

admin_mode = input("do you want to enter admin mode? yes/no : ")
if admin_mode == "yes":
    admin_password = input("enter admin password : ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated!")
    else :
        print("wrong password")
books = load_books()

book_count = int(input("How many books do you want to add? "))

for i in range(book_count):
    book = input("Enter a book: ")
    books.append(book)

show_books(books)

save_books(books)