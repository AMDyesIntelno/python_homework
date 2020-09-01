#编写程序,声明函数getValue(b,r,n),根据本金b,年利率r和年份n,计算最终收益
def getValue(b,r,n):
    return b*(1+r/100)**n
principal=int(input("请输入本金:"))
rate=float(input("请输入年利率:"))
years=int(input("请输入年份:"))
amount=getValue(principal,rate,years)
print("本金利率和为:%.2f"%amount)