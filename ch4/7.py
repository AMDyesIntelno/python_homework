#反倍数
n=int(input())
num=input().split()
a,b,c=int(num[0]),int(num[1]),int(num[2])
value=0
for i in range(1,n+1):
    if i%a and i%b and i%c:
        value+=1
print(value)