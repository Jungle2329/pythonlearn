class Student(object):
    # 类变量
    count = 0

    def __init__(self, name, score, time='8月'):
        # 实例变量
        self.__name = name
        self.__score = score
        self.time = time
        Student.count = Student.count + 1

    def __str__(self):
        return self.__name

    # 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    def __getattr__(self, item):
        if item == 'date':
            return '2018-11-2 12:23'
        if item == 'age':
            return lambda: 111
        return 'not get "' + item + '"'

    def my_print(self):
        print('name = %s score = %s' % (self.__name, self.__score))


sss = Student('zhangyi', '100')
print(sss.time)
print(sss.dat1e)
print(sss.age())

class Fib:
    def __init__(self):
        self.a, self.b = 1, 1

    # Fib()[2]
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

    # 可以被循环
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


# for x in Fib():
#     print(x)

print(Fib()[2])

# a = Student('zhangyi', 100, '8月')
# print(getattr(a, 'f', 'ad'))
# if hasattr(a, 'time'):
#     setattr(a, 'time', '10月')
# print(getattr(a, 'time'))
#
# a = getattr(a, 'my_print')


print(Student('zhangyi', 100))
s = Student('zhangyi1', 100, '8月')
print(s.count)
s = Student('zhangyi', 100, '8月')
print(s.count)


def set_gold(self, gold):
    self.gold = gold


# 给类动态添加方法，所有类的实例都有该方法
from types import MethodType

s = Student('zhangyi', 100)
s.set_gold = MethodType(set_gold, s)
s.set_gold(19)
print(s.gold)

# 给实例动态添加方法，只有该实例有该方法
Student.set_gold = set_gold
s = Student('zhangyi', 100)
s.set_gold(50)
print(s.gold)
s2 = Student('zhangyi', 100)
s2.set_gold(10)
print(s2.gold)


# 使用__slots__   只是针对实例变量和实例方法，对类变量和类的方法，或者类的子类都是没有作用的（重要）
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student2(object):
    __slots__ = ('name', 'age', 'gold')


s = Student2()
s.age = 5
s.name = 'zhangyi'
# 这里用slot限制了只能有name和age实例变量,所以gold会报异常
# 由于'gold'没有被放到__slots__中，所以不能绑定gold属性，试图绑定score将得到AttributeError的错误。
# s.gold = 110
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
# s.set_gold = MethodType(set_gold, s)
# s.set_gold(40)
# print(s.gold)

# python __slots__只能限制实例的属性及方法，对于类则没有影响，对于子类则更是没有限制。
Student2.set_gold = set_gold
Student2.title = 'shuang'
s2 = Student2()
s2.set_gold('100')
print(s2.gold)
print(s2.title)
