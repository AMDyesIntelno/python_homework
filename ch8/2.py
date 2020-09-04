def min_n(a,b,*c):
    m=min(a,b)
    if len(c):
        return(min(m,min(c)))
    else:
        return m
print("最小值为%d"%min_n(8,2,1,2,3,0))