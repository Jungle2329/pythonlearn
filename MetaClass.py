# 要创建一个class对象，type()函数依次传入3个参数：
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 使用type构造一个动态类，第一个参数是类名，第二个参数是父类Tuple，第三个参数是类的映射dict
Nihao = type('Nihao', (object,), dict(test=fn))

hello = Nihao()
hello.test()

# 元类
