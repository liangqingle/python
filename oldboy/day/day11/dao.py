#-*- coding:utf-8 -*-

"""
    堡垒机的数据库的操作部份
"""

import sqlalchemy

"""
下面是根据文档进行的学习
"""
def showVersion():
    return sqlalchemy.__version__

if __name__ == "__main__":
    print(showVersion())