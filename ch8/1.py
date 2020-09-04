#斐波那契数列
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1,21):
    print("%5d"%fib(i),end="")
    if i==10:
        print()