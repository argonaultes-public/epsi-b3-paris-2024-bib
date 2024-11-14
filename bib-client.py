# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 9999              # The same port as used by the server
 #EXPECTED: HELLO WORLD


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
        self.send_message(f'new|{title},{author},{content}')

    def delete_book(self):
        title = input('title: ')
        author = input('author: ')
        self.send_message(f'delete|{title},{author}')


    def list_books(self):
        self.send_message('list|')

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

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(bytes(message, 'UTF-8'))
            data = s.recv(1024)
        print('Received', repr(data))        

if __name__ == '__main__':
    bib = Bib()
    bib.run()