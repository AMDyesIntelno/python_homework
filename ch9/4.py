class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def info(self):
        print(self.__name,self.__age)
class Student(Person):
    def __init__(self,name,age,stu_id):
        Person.__init__(self,name,age)
        self.__stu_id=stu_id
    def info(self):
        Person.info(self)
        print(self.__stu_id)
p1=Person("zhangsan",18)
p2=Student("lisi",20,123456)
p1.info()
print("---")
p2.info()