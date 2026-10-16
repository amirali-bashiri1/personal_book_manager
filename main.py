from books import show_books


user_name = input("Enter your name: ")
print("Welcome", user_name)

book_count = int(input("How many books? "))

books = []

for i in range(book_count):
    book = input("Enter a book: ")
    books.append(book)

print("Your books:")
show_books(books)