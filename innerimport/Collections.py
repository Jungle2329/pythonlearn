from collections import namedtuple, deque, OrderedDict, ChainMap, Counter
import argparse, os

# collections模块提供了一些有用的集合类，可以根据需要选用。

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
a = Point(1, 2)
print(a.x)

# deque
dlist = deque([1, 2, 3, 4, 5])
dlist.append(10)
dlist.appendleft(11)
print(dlist)

# orderedDict
dt = dict([('a', 1), ('b', 2), ('c', 3)])
print(dt)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
odt = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(odt)
print(odt['a'])


# 实现一个先进先出的dict
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            # del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


ll = LastUpdateOrderedDict(5)
ll['a'] = 1
ll['b'] = 2
ll['c'] = 3
ll['d'] = 4
ll['e'] = 5
ll['f'] = 6
ll['b'] = 7
print(ll)

# ChainMap
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 接收命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
print(parser)
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
print(command_line_args)
# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

print('-------------------------------------')
a = ChainMap({'a': 'aaa', 'b': 'bbb'}, os.environ, defaults)
print(a['ALLUSERSPROFILE'])

# Counter
print('-------------------------------------')
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
