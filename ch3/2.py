#编写程序,计算Sn=1-3+5-7+9-11...
S=0
check=True
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        continue
    if check:
        S+=i
        check=False
    else:
        S-=i
        check=True
print(S)