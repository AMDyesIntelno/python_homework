def Int_to_Complement(n):#取补码
    return bin(0xffffffff&n).replace("0b","").zfill(32)
num=input().split()
a,b=int(num[0]),int(num[1])
a,b=Int_to_Complement(a),Int_to_Complement(b)
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
ans=int(ans,2)
if ans>=0x80000000:
    print(~(ans^0xffffffff))
else:
    print(ans)
'''
'''
a,b=int(num[0]),int(num[1])
def get_sum(a,b):
    a,b=a&0xffffffff,b&0xffffffff#取补码
    while b:
        up=(a&b)<<1#进位
        a^=b#求和
        b=up&0xffffffff#截断(例如当a=-1,b=-8时)
    if a>=0x80000000:
        return ~(a^0xffffffff)
    else:
        return a
print(get_sum(a,b))