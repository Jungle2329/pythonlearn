import logging


# try:
#     print('try...')
#     a = int('a') / 0
#     print('result:', a)
# except ValueError as e:
#     print('except1:', e)
# except ZeroDivisionError as e:
#     print('except2:', e)
# except BaseException as e:
#     print('except3:', e)
# else:
#     print('else')
# finally:
#     print('finally...')
# print('END...')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as exc:
        logging.exception(exc)


# main()


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


# bar()


from functools import reduce


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(add, ns)


def add(a, x):
    return lambda a, x: a + x


def main():
    r = calc(1, 2, 3)
    print(r)


main()
