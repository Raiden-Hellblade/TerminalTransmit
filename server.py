import socket

HOST = 0.0.0.0  # listen on all available network interfaces
PORT = 5000  # choose a port number that is not already in use

# create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}...')

# accept incoming connections and handle them one at a time
while True:
    client_socket, client_address = server_socket.accept()
    print(f'Client connected from {client_address[0]}:{client_address[1]}')

    # receive data from the client and send a response
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f'Received: {data.decode()}')
        client_socket.sendall(b'ACK')

    # clean up the connection
    client_socket.close()
    print(f'Client disconnected from {client_address[0]}:{client_address[1]}')
