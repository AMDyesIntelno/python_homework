from hashlib import md5
for i in range(128):
    for j in range(128):
        for k in range(128):
            s="AGVSCF"+chr(i)+"TZV"+chr(j)+"WBGVHC"+chr(k)+"U"
            h1=md5()
            h1.update(s)
            b=h1.hexdigest()
            if b[:6]=="a8f738":
                print(s)
                print(b)