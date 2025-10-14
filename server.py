import socket


host = '127.0.0.1'
port = int(input('Enter a port: '))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
con, addr = server.accept()


while True:
    data = con.recv(1024).decode()
    print(data)
    msg = input('Type a message: ')
    con.send(msg.encode())
