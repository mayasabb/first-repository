import constants

# The function print the menu
def print_menu():
    print(str(constants.ADD) + " - Add")
    print(str(constants.REMOVE) + " - Remove")
    print(str(constants.SEARCH) + " - Search")
    print(str(constants.PRINT_ALL) + " - Print all")
    print(str(constants.EXIT) + " - Exit")


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