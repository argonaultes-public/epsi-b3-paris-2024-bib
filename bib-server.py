import socketserver



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
        result = ''
        for book in self.__books:
            result = result + str(book) + '\n'
        return result
    
    def remove_book(self, book_to_remove):
        try:
            self.__books.remove(book_to_remove)
        except ValueError:
            print(f'Unable to remove {book_to_remove}')

class BookShop:

    def __init__(self):
        #TODO
        pass



class BibTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        lib = Lib() #TODO: get the previous state of Lib
        self.data = self.request.recv(1024).strip()

        print("Received from {}:".format(self.client_address[0]))
        print(self.data)
        actions = self.data.decode('UTF-8').split('|')
        result = ''
        print(actions)
        if actions[0] == 'new':
            title, author, content = actions[1].split(',')
            book = Book(title, author, content)
            lib.add_book(book)
            result = f'Book {book} added'
        if actions[0] == 'delete':
            title, author = actions[1].split(',')
            result = 'deleted'
        if actions[0] == 'list':
            result = lib.display_books()

        print(bytes(result, 'UTF-8'))
        # just send back the same data, but upper-cased
        self.request.sendall(bytes(result, 'UTF-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), BibTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()