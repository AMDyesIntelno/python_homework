class Person1:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name
a=Person1("zhangsan")
print(a.name)