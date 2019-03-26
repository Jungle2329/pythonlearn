import base64

b64 = base64.b64encode(b'zhangyi')
print(b64)
result = base64.b64decode(b'emhhbmd5aQ==')
print(result)

a = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(a)

b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)


def safe_base64_decode(s):
    return base64.urlsafe_b64decode(s + b'=' * (4 - len(s) % 4))


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

print(base64.urlsafe_b64decode(b'YWJjZA=='))
