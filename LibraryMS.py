# database
books = []
issued_books = []

# add function
def add_books():
    name = input("Enter the Book name: ").lower()

    if name in books:
        print("Book already exists!\n")
    else:
        books.append(name)
        print(name, "is added successfully!\n")

# show books
def show_books():
    if len(books) == 0:
        print("No books available\n")
    else:
        print("Available Books:")
        for b in books:
            print(b)
        print()

# issue books
def issue_books():
    if len(books) == 0:
        print("No Books Available!\n")
        return

    show_books()
    name = input("Enter book name to issue: ").lower()

    if name in books:
        books.remove(name)
        issued_books.append(name)
        print(name, "is issued successfully!\n")
    else:
        print(name, "is not available\n")

# return books
def return_books():
    if len(issued_books) == 0:
        print("No issued books\n")
        return

    print("Issued Books:")
    for b in issued_books:
        print(b)

    name = input("Enter book name to return: ").lower()

    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name, "returned successfully!\n")
    else:
        print("Invalid book name\n")

# main menu
def library():
    while True:
        print("====== LIBRARY MENU ======")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid choice\n")

library()