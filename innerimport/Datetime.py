from datetime import datetime, timedelta, timezone
import re

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
#
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

dt = datetime(2018, 1, 2, 3, 4, 5, 1123)
print(dt)
print(datetime.now())
dt = datetime.now()
print(type(dt))
timestamp = dt.timestamp()
print(timestamp)
print(datetime.fromtimestamp(timestamp))  # 本地时间
print(datetime.utcfromtimestamp(timestamp))  # UTC时间
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 格式化时间
a = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(datetime.strptime(a, '%Y-%m-%d %H:%M:%S'))  # 时间戳
datetime.utcfromtimestamp(datetime.strptime(a, '%Y-%m-%d %H:%M:%S').timestamp())

# 时间计算，时间计算智能用datetime类，不能使用时间戳
print('--------------------------')
times = datetime.timestamp(dt)
print(dt)
# print(times + timedelta(days=1))  错误的
print(dt + timedelta(days=1))
print(dt - timedelta(seconds=1))

print(datetime.utcnow())
tz_utc_8 = timezone(timedelta(hours=8))
print(datetime.now())
print(datetime.now().replace(tzinfo=tz_utc_8))

print('-----------时区转换------------')
utc_now = datetime.utcnow()
# replace强制设置时区
print(utc_now.replace(tzinfo=timezone.utc))
print(utc_now.replace(tzinfo=tz_utc_8))
print(utc_now.replace(tzinfo=timezone.min))
print(utc_now.replace(tzinfo=timezone.max))
print(utc_now.replace(tzinfo=(timezone(timedelta(hours=4, minutes=30)))))
# astimezone转换时区
print(utc_now.astimezone(timezone(timedelta(hours=8))))

# 问题
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
print('-----------练习------------')


def to_timestamp(dt_str, tz_str):
    dt_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    s = re.match(r'UTC(\+|-)(\d+):(\d{2})', tz_str)
    if '+' == s.group(1):
        tz = timezone(timedelta(hours=float(s.group(2)), minutes=float(s.group(3))))
    else:
        tz = timezone(timedelta(hours=-float(s.group(2)), minutes=-float(s.group(3))))
    return dt_dt.replace(tzinfo=tz).timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2


