def get_mark():
    print("请输入成绩(1~100),按q退出")
    mark=[]
    while 1:
        c=input()
        try:
            c=int(c)
        except ValueError:
            print(mark)
            return
        else:
            try:
                assert 1<=c<=100
            except AssertionError:
                print("输入有误,请重新输入")
            else:
                mark.append(c)
get_mark()