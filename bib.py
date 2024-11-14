
class Book:

    def __init__(self, name, author, content):
        self.__id = 0
        self.__name = name
        self.__author = author
        self.__content = content

    def __eq__(self, other):
        return self.__author == other._Book__author and self.__name == other._Book__name
    
    def __hash__(self):
        return hash((self.__name, self.__author))

class Lib:

    def __init__(self, current_id_book):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

class BookShop:

    def __init__(self):
        #TODO
        pass

class Bib:

    def __init__(self):
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

    def delete_book(self):
        id_book = input('id book to destroy: ')

    def list_books(self):
        print('list books')

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
