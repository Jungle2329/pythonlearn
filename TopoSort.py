# python多重继承所使用的拓扑排序c3算法

# Python中使用mixin来表示多重继承，可以看做是Java中的Interface
# 使用Mixin类实现多重继承要非常小心
#
# 首先它必须表示某一种功能，而不是某个物品，如同Java中的Runnable，Callable等
# 其次它必须责任单一，如果有多个功能，那就写多个Mixin类
# 然后，它不依赖于子类的实现
# 最后，子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能。（比如飞机照样可以载客，就是不能飞了^_^）

# 总结大概就是，带有Mixin的父类是一种单一的功能，不依赖子类实现(自己可以实现)，即使子类不继承mixin类也可以使用
# class C(A, MixinB)

class A(object):

    def bar(self):
        print('A bar')


class B(object):
    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A):
    pass


class C2Mixin(B):
    def bar(self):
        print('C2-bar')


class D(C1, C2Mixin):
    pass


if __name__ == '__main__':
    print(D.mro())
    d = D()
    d.bar()
    d.foo()
