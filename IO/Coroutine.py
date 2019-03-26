import threading
import asyncio
from asyncio import Future
from collections.abc import Generator, Coroutine

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


# 使用yield达成协程，协程是同一个线程中的
# c = consumer()
# produce(c)

def ioTask():
    return asyncio.sleep(1)


@asyncio.coroutine
def hello():
    print('helloworld%s' % threading.currentThread())
    yield from ioTask()
    print('helloworld%s' % threading.currentThread())


# task = [hello(), hello()]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))
# loop.close()


def test():
    a = 0
    yield from range(100)
    raise StopIteration


# a = test()
# print(getgeneratorstate(a))
# print(next(a))
# print(getgeneratorstate(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# a.close()
# print(getgeneratorstate(a))

# 嵌套使用
def average_gen():
    total = 0
    count = 0
    average = 0
    while 1:
        newNum = yield average
        if not newNum:
            break
        total += newNum
        count += 1
        average = total / count
    return total, count, average


def proxy_gen():
    while 1:
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))


def main():
    # 创建协程
    calc = proxy_gen()
    # 加载协程
    calc.send(None)
    print(calc.send(1))
    print(calc.send(2))
    print(calc.send(3))
    print(calc.send(4))
    print(calc.send(5))
    print(calc.send(6))
    print(calc.send(7))
    print(calc.send(8))
    print(calc.send(9))
    # 停止协程
    calc.send(None)


async def df():
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')
    await asyncio.sleep(1)
    print('4')


async def ff():
    print('5')
    await asyncio.sleep(1)
    print('6')
    await asyncio.sleep(1)
    print('7')
    await asyncio.sleep(1)
    print('8')
    pass


if __name__ == '__main__':
    # main()
    a = asyncio.ensure_future(asyncio.sleep(33))
    print(isinstance(a, Coroutine))
    print(isinstance(a, Future))
    print(isinstance(a, Generator))


