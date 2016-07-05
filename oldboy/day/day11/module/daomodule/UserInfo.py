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


from dao.dao import makebase
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


