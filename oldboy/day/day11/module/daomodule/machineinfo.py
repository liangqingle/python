#-*- coding:utf-8 -*-

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
