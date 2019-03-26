
# 使用@property和@xxx.setter方法显示属性的绑定
class Screen(object):

    # get方法
    @property
    def width(self):
        return self._width

    # set方法
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

    # 使用set/get方法
    def getVaule(self):
        return self._value

    def setValue(self, value):
        self._value = value


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

s.setValue(100)
print(s.getVaule())
