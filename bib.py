
class Book:

    def __init__(self, title, author, content):
        self.__title = title
        self.__author = author
        self.__content = content

    def __eq__(self, other):
        return self.__author == other._Book__author and self.__title == other._Book__title
    
    def __hash__(self):
        return hash((self.__title, self.__author))

    def __repr__(self):
        return f'Book[title: {self.__title}, author: {self.__author}]'

class Lib:

    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def display_books(self):
        for book in self.__books:
            print(book)
    
    def remove_book(self, book_to_remove):
        try:
            self.__books.remove(book_to_remove)
        except ValueError:
            print(f'Unable to remove {book_to_remove}')

class BookShop:

    def __init__(self):
        #TODO
        pass

class Bib:

    def __init__(self):
        self.__lib = Lib()
        self.actions = {
            'new': self.new_book,
            'delete': self.delete_book,
            'list': self.list_books,
            'help': self.display_help,
            'q': self.end_session
        }

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        self.__lib.add_book(Book(title, author, content))

    def delete_book(self):
        title = input('title: ')
        author = input('author: ')
        self.__lib.remove_book(Book(title, author, None))


    def list_books(self):
        self.__lib.display_books()

    def display_help(self):
        print('[new, delete, list, q (quit), help]')

    def end_session(self):
        exit()

    def run(self):
        while True:
            action = input('Choose action: ')
            if action not in self.actions.keys():
                print(f'Action [{action}] not supported')
            else:
                self.actions[action]()

if __name__ == '__main__':
    bib = Bib()
    bib.run()
