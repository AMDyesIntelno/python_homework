#删除一个list中的重复元素
s=[2,1,1,2,3,4,2,6,7,6]
print(list(set(s)))
#---
temp=[]
for i in range(len(s)):
    if s.index(s[i])<i:
        continue
    else:
        temp.append(s[i])
print(temp)
#---
temp=[]
for i in s:
    if i not in temp:
        temp.append(i)
print(temp)