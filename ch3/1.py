#输出2000~4000之间的所有闰年
j=0
for i in range(2000,4001):
    if i%400==0 or (i%4==0 and i%100!=0):
        j+=1
        print(i,end=" ")
        if j%18==0:
            print()