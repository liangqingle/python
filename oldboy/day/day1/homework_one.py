# -*- coding:utf-8 -*-

"""
    作业二：编写登陆接口
        输入用户名密码
        认证成功后显示欢迎信息
        输错三次后锁定
"""

from getpass import getuser, getpass

checkcount = 3
passflag = False
usernamelist = ["one","two","three","four","five"]
userpasswordlist = ["one","two","three","four","five"]

while checkcount>0:
    username_input = input("username:")
    userpassword_input = getpass()
    try:
        if userpassword_input == userpasswordlist[usernamelist.index(userpassword_input)]:
            passflag=True
            break
    except Exception:
        print("找不到密码")
    checkcount-=1

if passflag:
    print("登陆成功")
else:
    print("登陆失败")    