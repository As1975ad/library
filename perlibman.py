import json

# Function to initialize the library
def load_library():
    try:
        with open('library.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save library to a file
def save_library(library):
    with open('library.json', 'w') as file:
        json.dump(library, file)

# Function to add a book to the library
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read_status': read_status
    }
    library.append(book)
    print(f"✅ '{title}' has been added to the library.")

# Function to remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"🗑️ '{title}' has been removed from the library.")
            return
    print(f"❌ No book found with the title '{title}'.")

# Function to search for books
def search_books(library):
    search_term = input("Enter the title or author to search: ").strip().lower()
    found_books = [book for book in library if search_term in book['title'].lower() or search_term in book['author'].lower()]
    
    if found_books:
        print(f"\n🔎 Found {len(found_books)} book(s):")
        for book in found_books:
            print(f"- {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Status: {'Read' if book['read_status'] else 'Unread'}")
    else:
        print("❌ No books found matching your search.")

# Function to display all books in the library
def display_all_books(library):
    if not library:
        print("❌ No books in the library.")
    else:
        print("\n📚 All Books in the Library:")
        for book in library:
            print(f"- {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Status: {'Read' if book['read_status'] else 'Unread'}")

# Function to display library statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read_status'])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"📖 Books Read: {read_books}")
    print(f"✅ Read Percentage: {percentage_read:.1f}%")

# Function to handle the main menu
def main():
    library = load_library()

    while True:
        print("\n📚 Personal Library Manager")
        print("1️⃣ Add a Book")
        print("2️⃣ Remove a Book")
        print("3️⃣ Search for a Book")
        print("4️⃣ Display All Books")
        print("5️⃣ Display Statistics")
        print("6️⃣ Exit")

        choice = input("🔸 Choose an option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("👋 Goodbye! Library data has been saved.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



