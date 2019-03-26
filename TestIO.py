# 读取文件
# with open('F:\jungle\pythonTest\learn\io_test.txt', 'r', encoding='gbk', errors='ignore') as f:
#     for lines in f.readlines():
#         print(lines.strip())

# 写文件
# with open('F:\jungle\pythonTest\learn\io_test.txt', 'a') as f:
#     f.write('!!!\n')

from io import StringIO, BytesIO

f = StringIO('String\nis\nnewBee')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


b = BytesIO()
b.write('中国'.encode('utf-8'))
print(b.getvalue())
print(b.read())
# 写入字符串有光标的概念，写入后使用getvalue可以读取全部数据，
# 但是使用.read不能拿到数据，可以使用seek方法重置光标到开头
b.seek(0)
print(b.read())

c = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(c.read())

# 从下面这个例子可以看出在构造中传入的值最后光标是在最前，write添加的值光标在最后
# 假如没有seek（5）的时候新写入的456就会把123替换掉
f = StringIO("1\n2\n3\n")
f.seek(6)
f.write("4\n5\n")
f.seek(0)
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())