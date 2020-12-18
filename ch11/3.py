def fun(s,t):
    if len(s)!=len(t):
        return False
    dict_s={}
    dict_t={}
    for i in s:
        if i in dict_s:
            dict_s[i]+=1
        else:
            dict_s[i]=1

    for i in t:
        if i in dict_t:
            dict_t[i]+=1
        else:
            dict_t[i]=1
    return dict_t==dict_s

s=input()
t=input()
print(fun(s,t))