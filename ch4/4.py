#韩信点兵
print("0~1000中用3除余2,用5除余3,用7除余2的数有:")
for i in range(0,1001):
    if i%3==2 and i%5==3 and i%7==2:
        print(i,end=" ")