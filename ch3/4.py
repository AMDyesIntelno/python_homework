#编写程序,输入一元二次方程的三个系数a,b和c,求ax^+bx+c=0的解
a=float(input("请输入系数a:"))
b=float(input("请输入系数b:"))
c=float(input("请输入系数c:"))
if a==0 and b==0:
    print("此方程无解!")
elif a==0 and b!=0:
    print("此方程的解为: %.1f"%(-c/b))
elif b*b-4*a*c==0:
    print("此方程有两个相等实根: %.1f"%(-b/(2*a)))
elif b*b-4*a*c>0:
    print("此方程有两个不等实根: %.1f 和 %.1f"%((-b/(2*a)+((b*b-4*a*c)**0.5)/(2*a)),(-b/(2*a)-((b*b-4*a*c)**0.5)/(2*a))))
else:
    print("此方程有两个共轭复根: %.1f%+.1fi 和 %.1f%+.1fi"%(-b/(2*a),((4*a*c-b*b)**0.5)/(2*a),-b/(2*a),-((4*a*c-b*b)**0.5)/(2*a)))