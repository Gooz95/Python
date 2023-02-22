import sys

# Global arrays to be able to append and remove
book_list = ["Science Book",
             "Business Book",
             "History Book",
             "Medical Book",
             "Computer Science",
             "Engineering Book",
             "English Book"]

book_stocks = ["Science Book",
               "Business Book",
               "History Book",
               "Medical Book",
               "Computer Science",
               "Engineering Book",
               "English Book",
               "Fitness Book",
               "Cooking Book",
               "Programming Book",
               "Story Book",
               "Coding Book"]

# arrays of id and password to verify login
user_id = ["M123", "M321", "M112", "M221"]

user_password = ["123", "321", "112", "221"]

admin_list = ["A123", "A321", "A111", "A000"]


#####################################################
# library class with show all books function
class Library:

    def __init__(self):
        self.availablebooks = book_list

    # this function will iterate and display all books available
    def displayAvailablebooks(self):
        print("===The books we have available===")
        for book, element in enumerate(self.availablebooks, start=1):
            print("-", book, element)


# object to call functions within a class
library = Library()


#####################################################
# books class inheriting from Library
class Books(Library):
    # add book function allowing to add a book
    def add_book(self):
        print("===what book would you like to add===")
        for book, element in enumerate(book_list, start=1):
            print("-", book, element)
        user_input = input("Bookname: ").title()
        if user_input not in book_list:
            book_list.append(user_input)
            print(library.displayAvailablebooks())
            print(f"==={user_input} Added===")
        else:
            print("---Book not in our library---")

    # delete book function allows to delete book in list
    def delete_book(self):
        print("===What book would you like to delete===")
        for book, element in enumerate(book_list, start=1):
            print("-", book, element)
        user_input = input("Bookname: ").title()
        if user_input in book_list:
            book_list.remove(user_input)
            print(library.displayAvailablebooks())
            print(f"==={user_input} Removed===")
        else:
            print("---Choose from the list---")

    # edit book function allows to edit a book in list
    def edit_book(self):
        print("===What book would you like to edit===")
        for book, element in enumerate(book_list, start=1):
            print("-", book, element)
        user_input = input("Bookname: ").title()
        if user_input in book_list:
            book_list.remove(user_input)
            user_input = input("Enter new Bookname: ").title()
            if user_input not in book_list:
                book_list.append(user_input)
                print(library.displayAvailablebooks())
                print(f"==={user_input} Edited===")
            else:
                print("Bookname already taken")
        else:
            print("Book not in list")

    # search book function allows to search a book thats available in the library
    def search_book(self):
        print("What book would you like to search")
        user_input = input("- ").title()
        if user_input in book_list:
            print(f"{user_input} is available")
        else:
            print(f"{user_input} not available in this library")


# object to call functions within a class
book = Books()


##########################################################

# members class
class Members:

    def __init__(self):
        self.ID = user_id

    # display users functions allowing to show members
    def display_users(self):
        print("===User ID's===")
        for user, ele in enumerate(self.ID, start=1):
            print(user, "-ID-", ele)


# object to call functions within a class
members = Members()


#########################################################
# class user inheriting from Members
class User(Members):

    def __init__(self):
        pass

    # UI only for student once logged in
    def user_ui(self):

        while True:
            print("===Welcome to Birmingham Library===")
            print("""[1] Show All Books           
[2] Borrow Book
[3] Return Book
[4] Logout""")

            user_input = input("Please choose option: ")
            if user_input == "1":
                library.displayAvailablebooks()
            elif user_input == "2":
                users.borrow_book()
            elif user_input == "3":
                users.return_book()
            elif user_input == "4":
                main_menu()
            else:
                print("Choose from 1-5")
                continue

    # this function borrows book and removes the book from list
    def borrow_book(self):
        while True:
            print("___What book would you like to borrow?___")
            for i, element in (enumerate(book_list, start=1)):
                print("-", i, element)
            user_input = input("- ").title()
            if user_input in book_list:
                book_list.remove(user_input)
                print(f"==={user_input} has been borrowed===")
                break
            else:
                print("Please choose from the list of books")
                continue

    # this function allows to return book back to the library
    def return_book(self):
        while True:
            print("___What book would you like to return?___")
            for i, element in (enumerate(book_list, start=1)):
                print("-", i, element)
            user_input = input("- ").title()
            if user_input in book_stocks:
                book_list.append(user_input)
                print(f"{user_input} has been returned thank you!")
                break
            else:
                print("__Book is not from this library__")
                continue


# object to call functions within a class
users = User()


#####################################################


# class admin inheriting from Members
class Admin(Members):

    def __init__(self):
        pass

    # Admin ui options
    def admin_ui(self):
        while True:
            print("===Admin Menu===")
            print("""[1] Manage Members
[2] Manage Books
[3] Logout""")
            user_input = input("Choose options ")
            if user_input == "1":
                admin.admin_manage_members_ui()
            elif user_input == "2":
                admin.admin_manage_books_ui()
            elif user_input == "3":
                main_menu()
            else:
                print("Choose 1-3")
            continue

    # manage members option for admin
    def admin_manage_members_ui(self):
        while True:
            print("""[0] Display Members
[1] Add Members
[2] Delete Members
[3] Edit Members
[4] Back""")
            user_input = input("Please choose option: ")
            if user_input == "0":
                members.display_users()
            elif user_input == "1":
                admin.add_Member()
            elif user_input == "2":
                admin.delete_Member()
            elif user_input == "3":
                admin.edit_Member()
            elif user_input == "4":
                admin.admin_ui()
            else:
                print("Choose from 1-4")
                continue

    # Manage Books option for admin
    def admin_manage_books_ui(self):
        while True:
            print("""[0] Display Books
[1] Add Book
[2] Delete Book
[3] Edit Book
[4] Search Book
[5] Back""")
            user_input = input("Choose option: ")
            if user_input == "0":
                library.displayAvailablebooks()
            elif user_input == "1":
                book.add_book()
            elif user_input == "2":
                book.delete_book()
            elif user_input == "3":
                book.edit_book()
            elif user_input == "4":
                book.search_book()
            elif user_input == "5":
                admin.admin_ui()
            else:
                print("Choose from 1-3")
                continue

    # add member function allowing to add new member
    def add_Member(self):
        self.ID = user_id
        for user in self.ID:
            print("-", user)
        user_input = input("Enter new ID: ").title()
        if user_input not in user_id:
            user_id.append(user_input)
            print("Successfully Registered")
        else:
            print("ID already taken")

    # delete member function allows to delete a member
    def delete_Member(self):
        self.ID = user_id
        for user in self.ID:
            print("-", user)
        user_input = input("Enter ID to delete: ").title()
        if user_input in user_id:
            user_id.remove(user_input)
            print("Successfully Deleted")
        else:
            print("ID not found")

    # edit member functions allows to edit
    def edit_Member(self):
        print("===What ID would you like to edit===")
        for i in range(len(user_id)):
            print("-", user_id[i])
        user_input = input("ID: ").title()
        if user_input in user_id:
            user_id.remove(user_input)
            user_input = input("Enter new ID: ").title()
            if user_input not in user_id:
                user_id.append(user_input)
                print(f"==={user_input} Edited===")
            else:
                print("ID already taken")


# object to call functions within a class
admin = Admin()


######################################################

# Main menu function not in a class this is what you see when run this code
def main_menu():
    while True:
        print("""[1] Exit
[2] Member Login
[3] Admin Login""")
        user_input = input("Please choose option: ")
        if user_input == "1":
            print("===Hope to see you soon!===")
            sys.exit()

        elif user_input == "2":
            print("===Member Login===")
            user_input = input("Enter ID: ").title()
            if user_input in user_id:
                user_input = input("Enter Password: ").title()
                if user_input in user_password:
                    print("__Successful__")
                    users.user_ui()
                else:
                    print("__Unsuccessful__")
                    continue
            else:
                print(f"=={user_input} not found==")
                continue

        elif user_input == "3":
            print("Staff Login")
            user_input = input("Enter ID: ").title()
            if user_input in admin_list:
                print("_Successful_")
                admin.admin_ui()
            else:
                print(f"=={user_input} not found==")
                continue

        else:
            print("==Please choose from 1-3==")
            continue
main_menu()
