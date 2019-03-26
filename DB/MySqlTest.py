import mysql.connector
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


def createTable():
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        cursor.execute("create table user(id varchar(20) primary key, name varchar(20), age int)")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def dropDatabase():
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        cursor.execute('drop database test')
    finally:
        cursor.close()
        conn.close()


def insert(i):
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        cursor.execute("insert into user (id, name, age) values (%s, 'zhangyi' ,28)" % i)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        # 不进行事务操作没有用
        conn.commit()
        conn.close()


def delete(id):
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        cursor.execute('delete from user where id=%s' % id)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


def select():
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        cursor.execute("select * from user")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# createTable()
# insert(1)
# insert(2)
# insert(3)
# insert(4)
# insert(5)
# insert(6)
# insert(7)
# insert(8)
# insert(9)
# delete(3)
# select()

# ---------------ORM技术---------------
# ORM可以完成数据库和类的转化

Base = declarative_base()


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    job = relationship('job')


class Job(Base):
    __tablename__ = 'job'
    id = Column(String(20), primary_key=True)
    what = Column(String(20))


# 创建连接
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)


def createWithORM():
    session = DBSession()
    myJob = Job(id='11', what='basketball')
    myUser = User(id='11', name='LeBronJames', age=33, job=myJob)
    session.add(myUser)
    session.commit()
    session.close()


def selectWithORM():
    session = DBSession()
    user = session.query(User).filter(User.id == '10').one()
    print(user.age)
    session.close()


createWithORM()
