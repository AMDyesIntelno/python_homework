#自由落体计算
height=100.0
s=100.0
for i in range(1,10):
    s+=height
    height/=2
print("%.2f"%s)
print("%.2f"%(height/2))