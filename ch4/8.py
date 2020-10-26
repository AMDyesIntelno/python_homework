#字符串拼接
a = "字符串拼接1"
b = "字符串拼接2"
c=a+b
print(c)
c="%s%s"%(a,b)
print(c)
c="".join((a,b))
print(c)
c="{0}{1}".format(a,b)
print(c)
c=a+","+b
print(c)
c=a+b
print(len(c),c[7])