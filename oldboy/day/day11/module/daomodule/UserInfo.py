# -*- coding:utf-8 -*-

"""
    映射类
"""

import os
from os.path import realpath, dirname
import sys

REALPATH = os.path.realpath(__file__)
ROOTPATH = dirname(REALPATH)
ROOTPATH = dirname(ROOTPATH)
ROOTPATH = dirname(ROOTPATH)
sys.path.append(ROOTPATH)

from dao.dao import makebase, createall
from dao.dao import InsertDataBySession
from dao.dao import deletedatabysession
from dao.dao import changedatabysession
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
    
    info.password = "11"
    changedatabysession(info)

    deletedatabysession(info)
    
