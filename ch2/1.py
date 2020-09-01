#编写程序,输入本金,年利率和年份,计算复利(结果保留两位小数)
principal=int(input("请输入本金:"))
rate=float(input("请输入年利率:"))
years=int(input("请输入年份:"))
amount=principal*(1+rate/100)**years
print("本金利率和为:%.2f"%amount)