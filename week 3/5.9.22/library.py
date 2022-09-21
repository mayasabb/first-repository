ADD = 1
REMOVE = 2
SEARCH = 3
PRINT_ALL = 4
EXIT = 5


# The function get the library and name of book, and add it to the library
def add_book(library, book_name):
    if book_name not in library:
        library.append(book_name)


# The function get the library and name of book, and remove the book from the library
def remove_book(library, book_name):
    if book_name in library:
        library.remove(book_name)
        return True

    return False


# The function get the library and name of book, and add it to the library
def search_name(library, name_to_search):
    books_list = []
    name_to_search = name_to_search.lower()
    for key in library:
        if name_to_search in key.lower():
            books_list.append(key)
    return books_list


# The function print all the books in the library
def print_book_list(book_list):
    for i in range(len(book_list)):
        print(str(i + 1) + ". " + book_list[i])


# The function print the menu
def print_menu():
    print(str(ADD) + " - Add")
    print(str(REMOVE) + " - Remove")
    print(str(SEARCH) + " - Search")
    print(str(PRINT_ALL) + " - Print all")
    print(str(EXIT) + " - Exit")


def manage_library():
    my_library = []
    print("welcome to the library")
    print_menu()
    user_choice = int(input("Enter choice number"))

    while user_choice != EXIT:
        if user_choice == PRINT_ALL:
            print_book_list(my_library)
        else:
            book_name = input("Enter book name")
            if user_choice == ADD:
                add_book(my_library, book_name)
            elif user_choice == REMOVE:
                is_found = remove_book(my_library, book_name)
                if not is_found:
                    print("book does not exist")
            elif user_choice == SEARCH:
                result_list = search_name(my_library, book_name)
                if len(result_list) == 0:
                    print("book does not found")
                else:
                    print_book_list(result_list)
            else:
                print("choice doesn't found, please try again")

        print_menu()
        user_choice = int(input("Enter choice number"))


manage_library()

