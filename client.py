import socket


def client_input():
    global HOST, PORT
    print('[CONNECTION]: Waiting of the input')
    HOST = input('[IP_ADDRESS]: ')
    PORT = int(input('[PORT]: '))
    client_program()


def client_program():
    global HOST, PORT
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("[CONNECTION]: Connection with " + str(HOST))
        client_socket.connect((HOST, PORT))
        print("[CONNECTION]: Connected with " + str(HOST))
    except:
        print('[ERROR]: Please, try select another IP or port')
        client_input()
    message = input('[YOUR MESSAGE]: ')
    print('[DELIVERED]: ' + str(message))
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode('utf8'))
        data = client_socket.recv(1024).decode('utf8')
        print('[RECEIVED]:' + str(data))
        if data.lower().strip() == 'bye':
            break
        message = input('[YOUR MESSAGE]: ')
        print('[DELIVERED]: ' + str(message))
    client_socket.send(message.encode('utf8'))
    client_socket.close()
    print('[CONDITION]: Connection is stopped')
    exit()


if __name__ == '__main__':
    client_input()


