def calculate(a,b):
    try:
        a/b
    except ZeroDivisionError:
        print("Can't divide by zero!!!")
    else:
        print(a/b)
calculate(5,1)
calculate(5,0)