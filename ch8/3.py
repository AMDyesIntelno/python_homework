#利用元组作为函数的返回值,求其中的最大值,最小值和元素个数
def fun(l):
    return (max(l),min(l),len(l))
s1=[9,7,8,3,2,1,55,6]
s2=["apple","pear","melon","kiwi"]
s3="TheQuickBrownFox"
print("list=",s1)
print("最大值=%d,最小值=%d,元素个数=%d"%(fun(s1)[0],fun(s1)[1],fun(s1)[2]))
print("list=",s2)
print("最大值=%s,最小值=%s,元素个数=%d"%(fun(s2)[0],fun(s2)[1],fun(s2)[2]))
print("list=",s3)
print("最大值=%s,最小值=%s,元素个数=%d"%(fun(s3)[0],fun(s3)[1],fun(s3)[2]))