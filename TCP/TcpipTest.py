import socket


# Http协议测试
def client(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
    # s.send(b'GET / HTTP/1.1\r\nHost: ip\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if len(d):
            buffer.append(d)
        else:
            break

    data = b''.join(buffer)
    s.close()

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))

    with open('zhihu.html', 'wb') as f:
        f.write(html)


client('www.pythonlearn.com', 80)
