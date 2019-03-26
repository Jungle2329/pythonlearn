import os
import time
import random
from multiprocessing import Pool, Process, Queue, Pipe
import subprocess

print(os.getpid())
print(os.getppid())


# windows下没有fork方法
# pid = os.fork()


# windows下使用multiprocessing创建多进程
def startProcess(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(5)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, end - start))


# 直接使用多进程
# if __name__ == '__main__':
#     print('current process is %s' % os.getpid())
#     p = Process(target=startProcess, args=('test',))
#     print('Child process will start.')
#     p.start()  # 进程启动，一个对象只能启动一次
#     p.join()  # 等进程执行完再往下执行，相当于进程间的同步
#     print('Child process will start.')


# 使用进程池
# if __name__ == '__main__':
#     p = Pool(2)
#     for i in range(5):
#         p.apply_async(startProcess, args=(i,))  # 异步进程池
#         # p.apply(startProcess, args=(i,))  # 同步进程池
#     print('Waiting for all subprocesses done...')
#     p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#     p.join()  # 等进程执行完再往下执行，相当于进程间的同步
#     print('end')


# 子进程
if __name__ == '__main__':
    print('$nslookup www.python.org')
# 可以调用cmd中的功能
r = subprocess.call(
    ['adb', 'install', '-r', 'c:\\users\\administrator\\desktop\\smallpig\\smallpig2.0.0.apk'])
print('exit code', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output)
print('Exit code:', p.returncode)

p = subprocess.Popen(['adb'])


# 进程间通信
def read(p):
    print('Process to read: %s' % os.getpid())
    while True:
        value = p.get(True)
        print('Get %s from queue.' % value)


def write(p):
    print('Process to write: %s' % os.getpid())
    for i in ['A', 'B', 'C']:
        print('Put %s to queue...' % i)
        p.put(i)
        time.sleep(3)

# 进程间通信，使用Pipe或者是Quene
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()
