#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jungle'

import math
from collections import Iterable
from functools import reduce
import datetime
import time
import functools
import Student


def test():
    print('导入成功')


if __name__ == '__main__':
    test()


# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print(b'123'.decode('ascii'))
# print(b'\xe4\xb8\xad\xde'.decode('utf-8', errors='ignore'))
# print(b'\xe4\xb8\xad'.decode('utf-8'))
# print(len('中'.encode('utf-8')))
# print(len('a'.encode('ascii')))
# print('hello world %s' % 'zhangyi')
# print('hello %d %f' % (144, 144))
# a = 100
# if a >= 29:
#     print("fool")
# elif a >= 18:
#     print("adult")
# else:
#     print('child')
# if 1:
#     print('a')


# a = int(input('your birth year:'))
# if a == 1991:
#     print('zhangyi')
# else:
#     print("shabi")


# height = float(input('your height(m):'))
# weight = float(input('your weight(kg):'))
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# elif bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')


# names = ('zhangyi', 'fanyujie', 'liumang')
# for a in names:
#     print(a)

# L = ['Bart', 'Lisa', 'Adam']
# i = 0
# while i < len(L):
#     print(L[i])
#     i += 1


# sdf = (1, 2, 3)
# b = {sdf: '1', '1': '2'}
# print(b.get((1, 2, 3)))


# n1 = 255
# n2 = 1000
# print(str(hex(n1)))

# 参数的类型判断
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('shabia')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 计算 ax2 + bx + c = 0
def quadratic(a, b, c):
    k = b ** 2 - 4 * a * c
    if k >= 0:
        return (-b + math.sqrt(k)) / 2 / a, (-b - math.sqrt(k)) / 2 / a
    else:
        return '无解'


# 函数参数最好是不可变的，方式在多任务的情况发生混乱
def add_end(a=None):
    if a is None:
        a = []
    a.append('end')
    print(a)


# add_end()
# add_end()
# add_end()
# add_end([1, 2, 3])


# 把tuple当成可变参数
def calc_tuple(num):
    total = 0
    for n in num:
        total += n
    return total


# 直接使用可变参数
def calc(a, *num):
    total = 0
    for n in num:
        total += n
    return a, total


# my_tuple = (1, 2, 3, 4, 5)
# # 这里使用*把tuple变成了可变参数传入
# print(calc(*my_tuple))
# print(calc_tuple(my_tuple))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'kw:', kw)


# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('zhangyi', 27, **extra)


# 命名关键字参数
def person1(name, age, *agrs, city='taiyuan', job='fuweng'):
    print(name, age, agrs, city, job)


# a = [1, 2, 3]
# person1(1, 2, *a, job='program')

# 计算任意个数字的乘机
def product(*x):
    if len(x) == 0:
        raise TypeError("not empty tuple")
    total = 1
    for i in x:
        total *= i
    return total


# 递归函数
# 阶乘
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


# 尾递归，理论不会造成栈溢出，python没有优化过，所以还是会报出栈溢出
def fact1(x):
    return fact_iter(x, 1)


def fact_iter(num, total):
    if num == 1:
        return total
    return fact_iter(num - 1, total * num)


# 切片 切掉字符串两边所有的" "
def trim(x):
    if x[:1] == ' ':
        return trim(x[1:])
    elif x[-1:] == ' ':
        return trim(x[:-1])
    else:
        return x


# 查看是否可以迭代 from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance(123, Iterable))
# print(isinstance((1, 2, 3), Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance({1: 2, 2: 3}, Iterable))


# 带下标的迭代
a = {'name': 'zhangyi', 'age': 27}


# b = [1, 2, 3, 4, 5, 6]
# c = (1, 2, 3, 4, 5, 6)
# for i, value in enumerate(b):
#     print(i, value)

# d = [(1, 2), (4, 5)]
# for x1, x2 in d:
#     print(x1, '----', x2)


# 练习 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(l):
    if len(l) == 0:
        return None, None
    # 最大值
    x1 = l[0]
    # 最小值
    x2 = l[0]

    for i in l:
        if i > x1:
            x1 = i
        if i < x2:
            x2 = i
    return x2, x1


# b = {'name': 'zhangyi', 'age': 'twenty-seven'}
# # 列表生成式
# print([str(x) + '=' + str(y) for x, y in a.items()])
# print([str(x) for x in a.items()])
# print([x.upper() + '=' + y.lower() for x, y in b.items()])


# 筛选字符串
# L1 = ['Hello', 'World', 18, 'Apple', None]
# print([x for x in L1 if isinstance(x, str)])


# 生成器generator 斐波那契数列
def fib():
    a1, a2, n = 0, 1, 0
    while n < 10:
        yield a2
        a1, a2 = a2, a1 + a2
        n += 1
    return 'done'


# 生成器generator 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 高阶函数
# map       把第二个参数序列的每一个元素都以第一个参数的函数调用，生成一个生成器Iterator
#           map(f, [1, 2, 3, 4, 5, 6]) = [f(1), f(2), f(3), f(4), f(5), f(6)]
# reduce    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#           reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# filter    filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#           filter(f, [1, 2, 3, 4, 5, 6]) = [1, 3, 5]
# sorted    sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。key是一个函数，他会依次作用在序列上形成新序列，用这个新序列排序
#           sorted([1, -3 ,5 ,-2 ,4], key=abs, reverse=True)
#           sorted([1, -3 ,5 ,-2 ,4], key=abs)
#           sorted([1, -3 ,5 ,-2 ,4])
def f(x):
    return x * x


def r(x, y):
    return x * 10 + y


def char2num(x):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits.get(x)


# print(reduce(r, map(char2num, 'fff')))
# 用Lambda表达式
# print(reduce(lambda x, y: x * 10 + y, map(char2num, '37189273')))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    name = name.lower()
    a = [x for x in name]
    a[0] = a[0].upper()
    return ''.join(a)


# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda a, b: a * b, L)


# print(prod([1, 2, 3, 4]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    return reduce(lambda x, y: x * 10 + y, [int(x) for x in s.split('.')[0]]) + reduce(
        lambda x, y: x * 0.1 + y, [int(x) for x in s.split('.')[1][::-1]]) * 0.1


# print(str2float('1233.45632'))


# 在不使用任何库的情况下反转一个整数
def reserv(i):
    return int(reduce(lambda x, y: y + x, str(i)))


# print(reserv(123456))
# 求奇数
list(filter(lambda n: n % 2 == 1, range(20)))

# 把一个序列中的空字符串删掉
list(filter(lambda n: n and n.strip(), ['A', '', 'B', None, 'C', '  ']))


# 构造一个从3开始的奇数序列
def _odd_iter():
    i = 3
    while True:
        yield i
        i += 2


def _not_divisible(n):
    return lambda x: x % n != 0


# 计算素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# 计算回数
def is_palindrome(n):
    a = list(str(n))
    if len(a) == 1:
        return True
    i = 0
    while len(a) / 2 > i:
        i += 1
        if a[i] != a[len(a) - i - 1]:
            return False
    return True


# 计算回数
def is_palindrome1(n):
    a = list(str(n))
    a.reverse()
    return str(n) == ''.join(a)


# 计算回数
def is_palindrome2(n):
    return reduce(lambda x, y: y + x, str(n))


####################################################################################
# 返回函数
def lazy_sum(*args):
    def my_sum():
        num = 0
        for i in args:
            num += i
        return num

    return my_sum


# a = lazy_sum(1, 2, 3, 4, 5)
# print(a())


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# ，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 闭包修改
def count1():
    def f(i):
        def g():
            return i * i

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


# f1, f2, f3 = count1()
# print(f1())
# print(f2())
# print(f3())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    a = 0

    def counter():
        nonlocal a
        a += 1
        return a

    return counter


# a = createCounter()
# print(a())
# print(a())
# print(a())


# b = createCounter()
# print(b())
# print(b())
# print(b())
# print(b())
# print(b())


####################################################################################
# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
# 匿名函数可以作为返回值返回
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
def build(x, y):
    return lambda: x * x + y * y


# print(build(2, 3)())


####################################################################################
# 装饰器
# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 所以装饰器的模板代码


# 不带参数的装饰器
def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('func.name = %s ---------------------time = %s' % (func.__name__, nowtime))
        return func(*args, **kw)

    return wrapper


# 带参数的装饰器
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓开始↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            print('func.name = %s -----------%s---------time = %s' % (func.__name__, text, nowtime))
            my_func = func(*args, **kw)
            print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑结束↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
            return my_func

        return wrapper

    return decorator


# 计算函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.clock()
        my_func = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.clock() - start_time))
        return my_func

    return wrapper


# @metric
# def gaoxiao():
#     sum1 = 0
#     for a in range(5):
#         sum1 = sum1 + a
#     print(sum1)

# 偏函数，可以把大量需要调用的方法中的某些参数固定下来，如下方法就是把int函数的base参数始终设置为2
int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

# print(int2('10'))


ddd = Student('zhangyi', 100)
ddd.my_print()


def fn(self, name="world"):
    print('Hello %s' % name)

