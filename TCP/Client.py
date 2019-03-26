import socket


# socket客户端测试
import time


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 10086))
    print(s.recv(1024).decode('utf-8'))
    while True:
        content = input('输入传递的数据: ')
        if content == 'exit':
            s.close()
            break
        s.send(content.encode('utf-8'))
        buffer = []
        while True:
            d = s.recv(2)
            time.sleep(0.5)
            if len(d):
                buffer.append(d)
                print(buffer)
            else:
                break
        print(buffer)


client()
