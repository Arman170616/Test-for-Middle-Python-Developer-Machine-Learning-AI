import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create the books table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        published_year INTEGER
    )
''')

def add_book(title, author, published_year):
    cursor.execute('''
        INSERT INTO books (title, author, published_year)
        VALUES (?, ?, ?)
    ''', (title, author, published_year))
    conn.commit()
    print("Book added successfully.")

def get_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return books

def update_book(book_id, title, author, published_year):
    cursor.execute('''
        UPDATE books
        SET title = ?, author = ?, published_year = ?
        WHERE id = ?
    ''', (title, author, published_year, book_id))
    conn.commit()
    print("Book updated successfully.")

def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    print("Book deleted successfully.")

if __name__ == '__main__':
    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. Retrieve books")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            published_year = input("Enter the published year: ")
            add_book(title, author, published_year)
        elif choice == '2':
            books = get_books()
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
        elif choice == '3':
            book_id = input("Enter the ID of the book to update: ")
            title = input("Enter the new title: ")
            author = input("Enter the new author: ")
            published_year = input("Enter the new published year: ")
            update_book(book_id, title, author, published_year)
        elif choice == '4':
            book_id = input("Enter the ID of the book to delete: ")
            delete_book(book_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
