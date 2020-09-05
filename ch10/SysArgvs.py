def num(l):
    return len(l)
def out(l):
    for i in range(0,num(l)):
        print("sys.argv[%d]=%s"%(i,l[i]))