#user_create
import json
a={
    'username':'zhangsan',
    'password':'12345',
    'try_times':0,
    'lock':False
},{
    'username':'lisi',
    'password':'54321',
    'try_times':0,
    'lock':False
},{
    'username':'wangwu',
    'password':'45678',
    'try_times':0,
    'lock':False
}
js=json.dumps(a)

with open("users.json","w") as f:
    f.write(js)