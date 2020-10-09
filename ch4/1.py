a=[0,1,0]
for i in range(5):
    s=""
    for j in range(1,len(a)-1):
        s+=str(a[j])+" "
    print(s.center(20))
    b=[0]
    for j in range(len(a)-1):
        b.append(a[j]+a[j+1])
    b.append(0)
    a=b