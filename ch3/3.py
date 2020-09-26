#打印九九乘法表,上三角,下三角,矩形块
def print1():
    for i in range(1,10):
        for j in range(i,10):
            s=str(i)+"*"+str(j)+"="+str(i*j)
            print("%-7s"%s,end=" ")
        print()
def print2():
    for i in range(9,0,-1):
        print("%*s"%(8*(i-1),""),end="")
        for j in range(i,10):
            s=str(i)+"*"+str(j)+"="+str(i*j)
            print("%-7s"%s,end=" ")
        print()
def print3():
    for i in range(1,10):
        for j in range(1,10):
            s=str(i)+"*"+str(j)+"="+str(i*j)
            print("%-7s"%s,end=" ")
        print()
print1()
print("----------------------------------------------------------------------")
print2()
print("----------------------------------------------------------------------")
print3()