import json

# 生成
d = dict(name='zhangyi', age=27, score=100)
print(d)

print(json.dumps(d))

# 序列化到本地
with open('.\jsonText.txt', 'w') as f:
    json.dump(d, f)

# 从本地读取
with open('.\jsonText.txt', 'r') as f:
    print(json.load(f))

str = '{"code":1,"msg":"succeed","content":{"nickname":"\u9171\u72d7","avatar":"https:\/\/wx.' \
      'qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaEJ9lSXAA0lf3icju2zvNDV1eUrhXKX9BQsnZmwLEzoP' \
      '3ePiaNdoP4micauLGNweXTsg3yInj0cQ27ibUA\/132","cash_total":"0.00","count_partner":"0","' \
      'identity":1,"wx_bind":"1","wx_nickname":"\u9171\u72d7","agency_status":"0","store_stat' \
      'us":"10"}}'

jsonD = json.loads(str)
print(jsonD)
print(jsonD.get('content').get('avatar'))


class Person(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def person2dict(std):
    return {
        'name', std.name,
        'age', std.age,
        'score', std.score
    }


p = Person('zhangyiaaa', 27, 10000)
p_json = json.dumps(p, default=lambda obj: obj.__dict__)


def dict2person(d):
    return Person(d['name'], d['age'], d['score'])


# print(json.loads(jsonD, object_hook=dict2person))


def dict2student(d):
    return Person(d['name'], d['age'], d['score'])


zhangyi = json.loads(p_json, object_hook=dict2student)
print(zhangyi.age)

obj = dict(name='张轶', age=27)
print(json.dumps(obj, ensure_ascii=True))
print(json.dumps(obj, ensure_ascii=False))
print(json.dumps(obj))
jsonName = json.dumps(obj, ensure_ascii=False)
print(json.loads(jsonName).get('name'))

