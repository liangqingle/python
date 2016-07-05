#-*- coding:utf-8 -*-

"""
    堡垒机的数据库的操作部份
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connectstr = "sqlite:///:memory:"
engine = None
base = None
session = None
metadata = None


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
    global engine
    if engine == None:
        engine = sqlalchemy.create_engine(connectstr, echo=True)
    return engine


"""
    定义一个用于映射的基类
"""
def makebase():
    global base
    if base == None:
        base = declarative_base()
    return base


"""
    获取metadata
"""    
def getmetadata():
    global metadata
    if metadata == None:
        metadata = sqlalchemy.MetaData()
    return metadata


"""
    初始化表
"""    
def createall():
    makebase().metadata.create_all(getconnect()) 


"""
    删除表
"""
def dropall():
    makebase().metadata.drop_all(getconnect())


"""
    建立会话
"""    
def createSession():
    global session
    if session == None:
        session = sessionmaker(bind=getconnect())()    
    return session


"""
    关闭会话
"""    
def closesession():
    global session
    if session is not None:
        session.close()
    return 


"""
    插入数据
"""    
def InsertDataBySession(obj):
    tmpsession = createSession()
    tmpsession.add(obj)
    tmpsession.commit()


"""
    删除数据
"""
def deletedatabysession(obj):
    tmpsession = createSession()
    tmpsession.delete(obj)
    tmpsession.commit()

"""
    修改数据
"""
def changedatabysession(obj):
    tmpsession = createSession()
    tmpsession.add(obj)
    tmpsession.commit()


"""
    查询数据
"""    
def searchdatabysession(classname):
    tmpsession = createSession()
    queryobj=tmpsession.query(classname)
    tmpsession.commit()
    return queryobj


if __name__ == "__main__":
    print(showVersion())
