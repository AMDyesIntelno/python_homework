class fun:
    def fun1(self,name):
        print(name)
    def fun1(self,name,age):
        #method already defined line 2
        print(name,age)
a=fun()
#a.fun1("zhangsan")
a.fun1("lisi",22)
#Too many positional arguments for method 