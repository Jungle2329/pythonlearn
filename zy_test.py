# 计算2个数的公约数
def scale2(a, b):
    i = min(a, b)
    for x in reversed(range(1, i + 1)):
        if a % x == 0 and b % x == 0:
            a = a / x
            b = b / x
    print('a = %s , b = % s' % (a, b))


# 计算n个数的公约数
def scale(*a):
    lists = a
    i = min(a)
    flag = False
    for x in reversed(range(2, i + 1)):
        addd = list(lists)
        for y in addd:
            if y % x != 0:
                flag = True
                break

        if flag:
            flag = False
            continue

        result = []
        for se in lists:
            result.append(se / x)

        lists = result

    print(list(lists))


scale(360, 960)


def fn(self, name="world"):
    print('Hello %s' % name)


