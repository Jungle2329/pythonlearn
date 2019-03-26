import os


# 查找某一目录下的所有python文件

class FileDirOperation(object):

    @staticmethod
    def checkDir(path='.'):
        return [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

    @staticmethod
    def checkPythonFile(path='.'):
        return [x for x in os.listdir(path) if os.path.splitext(x)[1] == '.py']

    def check(self, path='.'):
        if len(self.checkPythonFile(path)) > 0:
            print(path)
            print(self.checkPythonFile(path))
            print('-' * 30)
        for x in self.checkDir(path):
            self.check(os.path.join(path, x))


if __name__ == '__main__':
    # print(FileDirOperation.checkPythonFile('.'))
    file = FileDirOperation()
    file.check()
