def fun1(s,t):
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

def fun2(s,t):
    if len(s)!=len(t):
        return False
    s=list(s)
    t=list(t)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if ord(s[i])>ord(s[j]):
                s[i],s[j]=s[j],s[i]
            if ord(t[i])>ord(t[j]):
                t[i],t[j]=t[j],t[i]
    return s==t

def fun3(s,t):
    return sorted(s)==sorted(t)

s=input()
t=input()
print(fun1(s,t))
print(fun2(s,t))
print(fun3(s,t))