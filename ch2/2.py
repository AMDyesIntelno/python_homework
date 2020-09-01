#编写程序,输入球的半径,计算球的表面积和体积
from math import pi
r=float(input("请输入球的半径:"))
S=4*pi*r**2
V=4/3*pi*r**3
print("球的表面积为:%.2f,体积为:%.2f"%(S,V))