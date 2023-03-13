import socket

HOST = 'xxx.xxx.xxx.xxx'  # replace with the server's public IP address
PORT = 5000  # replace with the server's port number

# create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
client_socket.connect((HOST, PORT))
print('Connected to server...')

# send data to the server and receive a response
while True:
    message = input('Enter a message: ')
    if not message:
        break
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f'Received: {data.decode()}')

# clean up the connection
client_socket.close()
