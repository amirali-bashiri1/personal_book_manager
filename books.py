def show_books(books):
    for book in books:
        print(f"Book: {book['name']} | Priority: {book['priority'].upper()}")
        print("----------------")


def save_books(books):
    import json

    with open("books.json", "w") as file:
        json.dump(books, file)


def load_books():
    import json

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []