#编写程序,提示输入姓名和出生年份,输出姓名和年龄
import datetime
name=input("请输入您的姓名:")
year=int(input("请输入您的出生年份:"))
age=datetime.date.today().year-year
print("您好!%s,您%d岁"%(name,age))