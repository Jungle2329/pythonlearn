import time, threading, multiprocessing


def loop():
    print('currentThread->', threading.current_thread().name)
    for i in range(3):
        print('currentThread %s -> %s' % (i, threading.current_thread().name))
        time.sleep(1)


# if __name__ == '__main__':
#     print('currentThread->', threading.current_thread().name)
#     t = threading.Thread(target=loop, name='LoopThreadHHH')
#     t.start()
#     t.join()
#     print('end')
#     print('currentThread->', threading.current_thread().name)

# 线程和进程最大的区别就是，线程之间的变量共享，进程之间各自的变量独立，而在多线程开发过程中，公共的变量数据有危险

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(i)
        finally:
            lock.release()


# if __name__ == '__main__':
#     aThread = threading.Thread(target=run_thread, args=(3,))
#     bThread = threading.Thread(target=run_thread, args=(8,))
#     aThread.start()
#     bThread.start()
#     aThread.join()
#     bThread.join()
#     print(balance)

def deadLoop():
    i = 0
    while True:
        i = i ^ 1


# 多线程使用，但是不能利用多核cpu
# if __name__ == '__main__':
#     for i in range(multiprocessing.cpu_count()):
#         a = threading.Thread(target=deadLoop)
#         a.start()

# 利用多核cpu直接搞满cpu
# if __name__ == '__main__':
#     p = multiprocessing.Pool(multiprocessing.cpu_count())
#     for i in range(multiprocessing.cpu_count()):
#         p.apply_async(deadLoop)
#     p.close()
#     p.join()

local_num = threading.local()


def calu():
    std = local_num.name  # 读取ThreadLocal变量
    print('print----%s' % std)


def subThread(name):
    local_num.name = name  # 保存ThreadLocal变量
    calu()


# 线程安全变量
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，
# 但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
# if __name__ == '__main__':
#     a = threading.Thread(target=subThread, args=('zhangyi',))
#     b = threading.Thread(target=subThread, args=('fanyujie',))
#     a.start()
#     b.start()
#     a.join()
#     b.join()
