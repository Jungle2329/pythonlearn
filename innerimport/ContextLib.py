from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('zhangyi') as q:
    q.query()

print('---------------------------------------')


# 使用@contextmanager
class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_quest(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')


with create_quest('zhangyi') as q:
    q.query()

print('---------------------------------------')


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('hello')
    print('world')

print('---------------------------------------')

# closing
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
