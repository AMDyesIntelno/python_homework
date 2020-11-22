def fib_rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)
def fib(n):
    ans=[]
    for i in range(n+1):
        if i==0:
            ans.append(0)
        elif i==1:
            ans.append(1)
        else:
            ans.append(ans[i-1]+ans[i-2])
    return ans
for i in range(1,21):
    print("%5d"%fib_rec(i),end="")
    if i==10:
        print()
print("\n---------------------------------------------------")
fib_list=fib(20)
for i in range(1,21):
    print("%5d"%fib_list[i],end="")
    if i==10:
        print()
print()