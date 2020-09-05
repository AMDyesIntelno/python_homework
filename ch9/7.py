#创建类Temperature,包含成员变量degree(表示温度)以及实例方法ToFahrenheit和ToCelsius
class Temperature:
    def __init__(self,degree):
        self.degree=degree
    def ToFahrenheit(self):
        return (self.degree*9/5)+32
    def ToCelsius(self):
        return (self.degree-32)*5/9
d=float(input("请输入摄氏温度: "))
T=Temperature(d)
print("摄氏温度=%.1f,华氏温度=%.1f"%(d,T.ToFahrenheit()))
d=float(input("请输入华氏温度: "))
T=Temperature(d)
print("摄氏温度=%.1f,华氏温度=%.1f"%(T.ToCelsius(),d))