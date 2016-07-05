#-*- coding:utf-8 -*-

import os
from os.path import realpath, dirname
import sys

REALPATH = os.path.realpath(__file__)
ROOTPATH = dirname(REALPATH)
ROOTPATH = dirname(ROOTPATH)
ROOTPATH = dirname(ROOTPATH)
sys.path.append(ROOTPATH)


from UserInfo import userinfo
from dao.dao import searchdatabysession
from dao.dao import InsertDataBySession
from dao.dao import deletedatabysession
from dao.dao import changedatabysession
from dao.dao import createall

"""
    建立对象
"""
info = userinfo(username="liangqingle", 
                fullname="liangqingle", 
                password="123"
               )        
"""
    初始化表
"""
createall()

"""
    插入单条记录
"""
InsertDataBySession(info)

"""
    修改数据
"""
info.password = "11"

"""
    修改记录
"""
changedatabysession(info)

"""
    查询数据
"""
searchdatabysession(userinfo)

"""
    删除数据
"""
deletedatabysession(info)
    
