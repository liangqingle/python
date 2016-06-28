# -*- coding:utf-8 -*-

"""
    映射类
"""

from dao import makebase, InsertDataBySession, createall, closesession, 
from sqlalchemy import Column, Integer, String


class userinfo(makebase()):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    fullname = Column(String)
    password = Column(String)


    def __repr__(self):
        return "<userinfo(username='%s', fullname='%s', password='%s')>"\
        %(self.username, self.fullname, self.password)


if __name__ == "__main__":
    info = userinfo(username="liangqingle", fullname="liangqingle", password="123")        
    print(info)
    createall()
    InsertDataBySession(info)


