#-*- coding:utf-8 -*-

"""
    堡垒机的数据库的操作部份
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

connectstr = "sqlite:///:memory:"
connect = None
base = None


"""
    下面是根据文档进行的学习
"""


"""
    显示sqlalchemy版本信息
"""
def showVersion():
    return sqlalchemy.__version__


"""
    进行连接
    方法会返回一个engine的实例。
    engine表示通过数据库语法处理细节的核心接口
"""
def getconnect():
    if connect == None:
        connect = sqlalchemy.create_engine(connectstr, echo=True)
    return connect


"""
    定义一个用于映射的基类
"""
def makebase():
    global base
    if base == None:
        base = declarative_base()
    return base

"""
    从映射基类中派生出一个映射类	
"""
def createUser():
    from sqlalchemy import Column, Integer, String
    tmpbase = makebase()
    class User(tmpbase):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)

        def __repr__(self):
        	return "<User(username='%s' fullname='%s' password='%s')>"\
        	       %(self.username, self.fullname, self.password)
    return User

if __name__ == "__main__":
    print(showVersion())
    print(createUser())