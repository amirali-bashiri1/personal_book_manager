from books import show_books, save_books, load_books

user_name = input("Enter your name: ")
print("Welcome", user_name)

books = load_books()

book_count = int(input("How many books do you want to add? "))

for i in range(book_count):
    book = input("Enter a book: ")
    books.append(book)

show_books(books)

save_books(books)