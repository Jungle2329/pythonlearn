import sqlite3
import os


# sqlite数据库测试
def dbCraete():
    # 打开数据库
    conn = sqlite3.connect('myDB.db')
    # 创建游标
    cursor = conn.cursor()
    # 执行语句
    cursor.execute('create table college (id varchar(20) primary key, school varchar(20))')
    cursor.execute('insert into college (id, school) values(\'1\',\'太原科技大学\')')
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭数据库
    conn.close()


def dbSelect():
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    cursor.execute('select * from college where id=?', ('3',))
    value = cursor.fetchall()
    print(value)
    cursor.close()
    conn.close()


def dbInsert():
    conn = sqlite3.connect('myDB.db')
    cursor = conn.cursor()
    cursor.execute('insert into college values(\'3\',\'北京大学\')')
    cursor.close()
    conn.commit()
    conn.close()


# dbCraete()
# dbSelect()
# dbInsert()

db_file = os.path.join(os.path.dirname(__name__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    selectConn = sqlite3.connect(db_file)
    selectCursor = selectConn.cursor()
    try:
        selectCursor.execute(r"select name from user where score between ? and ? order by score",
                             (low, high))
        result = selectCursor.fetchall()
        result = list(map(lambda x: x[0], result))
        return result
    except Exception as e:
        print(e)
    finally:
        selectCursor.close()
        selectConn.close()


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print(get_score_in(0, 100))
