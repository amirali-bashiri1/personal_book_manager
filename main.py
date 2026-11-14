import os
from dotenv import load_dotenv
from books import show_books, save_books, load_books

load_dotenv()

user_name = input("Enter your name: ")
print("Hello", user_name, "- Welcome to Personal Book Manager!")

admin_mode = input("do you want to enter admin mode? yes/no : ")

if admin_mode == "yes":
    admin_password = input("enter admin password : ")

    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated!")
    else:
        print("wrong password")

books = load_books()

book_count = int(input("How many books do you want to add? "))

for i in range(book_count):
    book_name = input("Enter a book: ")

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ").lower()

    book = {
        "name": book_name,
        "priority": priority
    }

    books.append(book)

show_books(books)

print("----------------")
print(f"Total number of books: {len(books)}")

save_books(books)