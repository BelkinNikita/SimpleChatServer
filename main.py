import server
import client


def statement_choosing():
    choice = input('[CHOICE] Hello! Are you server or client? 1/2:')
    if choice == '1':
        print('[Condition]: You are a server')
        server.server_program()
        exit()
    if choice == '2':
        print('[Condition]: You are a client')
        client.client_input()
        exit()
    if choice != 1 and 2:
        print('[ERROR]: Program has got an unrecognized response. Please, give an another answer.')
        statement_choosing()


statement_choosing()





