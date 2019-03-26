import logging
import pdb

logging.basicConfig(level=logging.INFO)


# 调试方法
# 1.print()

# 2.assert
def foo1(s):
    n = int(s)
    # assert n != 0, 'fuck'
    logging.info('n = %s' % n)
    return 10 / n


# 3.logging
def foo2(s):
    n = int(s)
    # assert n != 0, 'fuck'
    logging.info('n = %s' % n)
    return 10 / n


# 4.pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
