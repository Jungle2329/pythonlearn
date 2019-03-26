import hashlib, random

# md5
md5_1 = hashlib.md5()
md5_1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_1.hexdigest())

md5_2 = hashlib.md5()
md5_2.update('how to use md5 in '.encode('utf-8'))
md5_2.update('python hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())

# sha1
sha1_1 = hashlib.sha1()
sha1_1.update('zhangyi'.encode('utf-8'))
print(sha1_1.hexdigest())

sha1_2 = hashlib.sha1()
sha1_2.update('zhang'.encode('utf-8'))
sha1_2.update('yi'.encode('utf-8'))
print(sha1_2.hexdigest())


# 验证用户登录
def get_md5(keyword):
    return hashlib.md5(keyword.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
