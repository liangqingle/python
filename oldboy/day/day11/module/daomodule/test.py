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
    ��������
"""
info = userinfo(username="liangqingle", 
                fullname="liangqingle", 
                password="123"
               )        
"""
    ��ʼ����
"""
createall()

"""
    ���뵥����¼
"""
InsertDataBySession(info)

"""
    �޸�����
"""
info.password = "11"

"""
    �޸ļ�¼
"""
changedatabysession(info)

"""
    ��ѯ����
"""
searchdatabysession(userinfo)

"""
    ɾ������
"""
deletedatabysession(info)
    
