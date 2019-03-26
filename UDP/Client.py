import socket


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i = input('input')
    s.sendto(i.encode('utf-8'), ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
    s.close()


client()
