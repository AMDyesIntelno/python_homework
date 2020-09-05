#创建类MyMath,计算圆的周长,面积和球的表面积,体积
from math import pi
class MyMath:
    def __init__(self,r):
        self.r=r
    def circle_perimeter(self):
        return 2*pi*self.r
    def circle_area(self):
        return pi*self.r**2
    def ball_area(self):
        return 4*pi*self.r**2
    def ball_volume(self):
        return (4/3)*pi*self.r**3
r=float(input("请输入半径: "))
a=MyMath(r)
print("圆的周长=%.2f"%a.circle_perimeter())
print("圆的面积=%.2f"%a.circle_area())
print("球的表面积=%.2f"%a.ball_area())
print("球的体积=%.2f"%a.ball_volume())