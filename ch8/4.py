def fun(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)<len(b):
        print(b)
    else:
        print(a)
        print(b)
fun("asdf","123")
fun("123","asdf")
fun("asdf","1234")