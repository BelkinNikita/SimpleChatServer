import socket


def server_program():
    PORT = (int(input('[PORT_CHOOSING] Please, choose your Internet Port (1024-65535]: ')))
    HOST = socket.gethostname()
    print("[IP_ADDRESS]: {} \n[PORT]: {}\n[CONDITION] Server is on".format(socket.gethostbyname(HOST), PORT))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    connection, address = server_socket.accept()
    print("[CONNECTION]: Connected with " + str(address))
    while True:
        data = connection.recv(1024).decode('utf8')
        print('[RECEIVED]:' + str(data))
        data = input('[YOUR MESSAGE]: ')
        print('[DELIVERED]: ' + str(data))
        connection.send(data.encode('utf8'))
        if data.lower().strip() == 'bye':
            break
    connection.close()
    print('[CONDITION]: Server is off')


if __name__ == '__main__':
    server_program()