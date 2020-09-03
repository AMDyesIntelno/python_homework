#计算党费
salary=int(input("请输入有固定工资收入的党员的月工资: "))
if salary<=400:
    f=0.005*salary
elif salary<=600:
    f=0.01*salary
elif salary<=800:
    f=0.015*salary
elif salary<=1500:
    f=0.02*salary
else:
    f=0.03*salary
print("月工资 = %d ,交纳党费 = %.1f"%(salary,f))