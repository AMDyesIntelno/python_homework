import datetime


class Student:
    def __init__(self, name, number, birthday):
        self.name = name
        self.number = number
        self.birthday = birthday.split(
            "-")  #Sample:2000-01-01 -> ['2000', '01', '01']

    def get_student_age(self):
        now = (datetime.datetime.now().strftime("%Y-%m-%d")).split("-")
        for i in range(3):
            self.birthday[i] = int(self.birthday[i])
            now[i] = int(now[i])
        if self.birthday[1] < now[1]:  #如果今天日期大于等于生日
            return now[0] - self.birthday[0]
        elif self.birthday[1] == now[1]:
            if self.birthday[2] <= now[2]:  #如果今天日期大于等于生日
                return now[0] - self.birthday[0]
            else:
                return now[0] - self.birthday[0] - 1
        else:  #如果今天日期小于生日
            return now[0] - self.birthday[0] - 1


student_1 = Student("zhangsan", "123", "2000-01-01")
student_2 = Student("zhangsan", "123", "2000-12-01")
student_3 = Student("zhangsan", "123", "2000-12-06")
student_4 = Student("zhangsan", "123", "2000-12-07")
print(student_1.get_student_age())
print(student_2.get_student_age())
print(student_3.get_student_age())
print(student_4.get_student_age())