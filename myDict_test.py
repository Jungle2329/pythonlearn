from myDict import MyDict
import unittest


# 编写单元测试
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，
# 我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：
class TestDict(unittest.TestCase):

    # 必须以test开头
    def test_init(self):
        abs()
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_attr(self):
        d = MyDict()
        d['value'] = 'zhangyi'
        self.assertEqual(d.value, 'zhangyi')

    def test_err(self):
        d = MyDict(a='0')
        # self.assertEqual(d.a, '0')
        with self.assertRaises(ValueError):
            value = d.f

    def test_normal(self):
        a = 7
        if a < 1 or a > 5:
            print('123')
        else:
            print('error')

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')
