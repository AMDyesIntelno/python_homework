#login
import json
import getpass
import time
users_detial=None
with open("users.json") as f:
    users_detial=json.load(f)
username=input("用户名:")
passwd=getpass.getpass("密码:")
for i in range(len(users_detial)):
    if username==users_detial[i]['username']:
        if users_detial[i]['lock']==True:
            print("多次输入错误密码,该用户已被锁定")
        else:
            if passwd==users_detial[i]['password']:
                users_detial[i]['try_times']=0
                print("登陆成功")
            else:
                print("密码错误")
                users_detial[i]['try_times']+=1
                if users_detial[i]['try_times']==3:
                    print("多次输入错误密码,该用户已被锁定")
                    users_detial[i]['lock']=True
                    with open("warnlog.txt","a") as f:
                        f.writelines("[warning] %s - Password error three times - "%(username)+time.asctime(time.localtime(time.time()))+"\n")
            js=json.dumps(users_detial)
            with open("users.json","w") as f:
                f.write(js)
        exit(0)
with open("warnlog.txt","a") as f:
    f.writelines("[error] %s is not exist - "%(username)+time.asctime(time.localtime(time.time()))+"\n")
print("不存在该用户")