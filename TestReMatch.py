import re

std = r'1866f6fa54f6d546f5a4d6f6a5d4f6'
print(re.match(r'([0-9]*)[a-z]([0-9]*)', std).groups())
print(re.split(r'[a-zA-Z]+', std))

b = re.split(r'[\s;]+', 'ab c   ;f;f;; d')
print(b)

# 贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 预编译
mCompile = re.compile(r'^(\d+?)(0*)$')
print(mCompile.match('452112021112110000').groups())


def is_valid_email(addr):
    if re.match(r'[\w.]+@([\w]+?).[a-zA-Z]', addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')


def name_of_email(addr):
    if addr.startswith(r'<'):
        return re.match(r'(<)([a-zA-Z\s]+)(>)', addr).group(2)
    else:
        return re.split(r'@', addr)[0]


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
