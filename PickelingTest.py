import pickle

d = dict(name="zhangyi", age=28, score=100)

# 序列化
a = pickle.dumps(d)
print(a)

# 序列化到本地文件
f = open('.\dumps.txt', 'wb')
pickle.dump(d, f)
f.close()

# 读取序列化
with open('.\dumps.txt', 'rb') as f:
    print(pickle.load(f))


# 查看文件源码
with open(pickle.__file__, 'r') as ff:
    print(ff.read())
