#输入字符串,以列表形式输出每个字符的ascii码
s=input("请输入字符串:")
l=[]
for i in s:
    l.append(ord(i))
print(l)