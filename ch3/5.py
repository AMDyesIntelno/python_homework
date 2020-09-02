#编写程序,输入非负整数n,分别利用for循环和while循环求n!
n=int(input("请输入非负整数n:"))
while n<0:
    n=int(input("请输入非负整数n:"))
s=1
for i in range(1,n+1):
    s*=i
print("  for循环: %d! = "%n+str(s))
s=1
print("while循环: %d! = "%n,end="")
while n>0:
    s*=n
    n-=1
print(str(s))