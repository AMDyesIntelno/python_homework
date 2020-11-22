def bin2dec(b):
    b=list(b)[::-1]
    ans=0
    for i in range(len(b)):
        ans+=int(b[i])*2**i
    return ans
def dec2bin(d):
    d=int(d)
    ans=""
    while d//2:
        ans+=str(d%2)
        d//=2
    ans+=str(d%2)
    ans=ans[::-1]
    return ans
print(bin2dec("10100"))
print(dec2bin(20))
print(int("10100",2))
print(bin(20)[2:])