import getpass
username=input("用户名:")
passwd=getpass.getpass("密码:")
if username=="zhangsan" and passwd=="123456":
    print("登陆成功")
else:
    print("登陆失败")