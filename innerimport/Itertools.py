import itertools
from time import sleep
from functools import reduce

natuals = itertools.count(1, 2)
# for x in natuals:
#     sleep(1)
#     print(x)

cs = itertools.cycle('abc')
# for x in cs:
#     print(x)
#     sleep(1)

ns = itertools.repeat('haha', 10)
# for x in ns:
#     sleep(1)
#     print(x)

# 使用takewhile截取无线数列
a = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(a))

# chain迭代对象叠加
print(list(itertools.chain('abc', 'xyz')))

"""groupby()把迭代器中相邻的重复元素挑出来放在一起："""
print(list(itertools.groupby('AaABbBCCAaA', lambda c: c.upper())))
for x, key in itertools.groupby('AaABbBCCAaA', lambda c: c.upper()):
    print(x, list(key))

"""    
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
"""


def getPi(n):
    list_n = itertools.takewhile(lambda x1: x1 <= 2 * n - 1, itertools.count(1, 2))
    rc = itertools.cycle([4, -4])
    list_n = map(lambda j: next(rc) / j, list_n)
    return sum(list_n)


print(getPi(10))
