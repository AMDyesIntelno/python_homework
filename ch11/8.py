import random
a=set()
b=set()
for i in range(0,10):
    a.add(random.randint(0,10))
    b.add(random.randint(0,10))
print("集合的内容,长度,最大值,最小值分别为:")
print(a,len(a),max(a),min(a))
print(b,len(b),max(b),min(b))
print("a和b的并集,交集和差集分别为:")
print(a.union(b),a.intersection(b),a.difference(b))