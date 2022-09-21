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