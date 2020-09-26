#编写程序,产生两个0~100之间的随机整数a和b,求这两个整数的最大公约数和最小公倍数
import random
a=random.randint(0,100)
b=random.randint(0,100)
while a==0 or b==0:
    a=random.randint(0,100)
    b=random.randint(0,100)
print("整数1 = %d,整数2 = %d"%(a,b))
m,n=max(a,b),min(a,b)
while m%n!=0:
    m,n=n,m%n
print("最大公约数 = %d,最小公倍数 = %d"%(n,a*b/n))