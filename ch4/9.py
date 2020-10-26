def InttoComplement(n):
    return bin(0xffffffff&n).replace("0b","").zfill(32)
num=input().split()
a,b=int(num[0]),int(num[1])
a,b=InttoComplement(a),InttoComplement(b)
print(a,b)
out=[]
c=0
for i in range(31,-1,-1):
    if int(a[i])^int(b[i]):
        out.append(str(1^c))
        c=1&c#进位
    else:
        out.append(str(c))
        c=int(a[i])&int(b[i])#进位
out=out[::-1]
ans="0b"
for i in range(32):
    ans+=out[i]
print(int(ans,2))