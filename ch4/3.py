#鸡兔同笼
h=int(input("请输入总头数: "))
f=int(input("请输入总脚数(必须时偶数): "))
while f%2:
    f=int(input("请输入总脚数(必须时偶数): "))
def fun1(h,f):
    r=f/2-h
    c=h-r
    if r>=0 and c>=0:
        print("方法一: 鸡: %d只,兔: %d只"%(c,r))
    else:
        print("方法一: 无解,请重新运行测试")
fun1(h,f)
def fun2(h,f):
    for c in range(0,h+1):
        if 4*h-2*c==f:
            print("方法二: 鸡: %d只,兔: %d只"%(c,h-c))
            return
    print("方法二: 无解,请重新运行测试")
fun2(h,f)