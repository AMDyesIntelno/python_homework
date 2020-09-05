#!/usr/bin/python3
import sys
def sequentialSearch(l,item):
    pos=0
    found=False
    while pos<len(l) and not found:
        if str(l[pos])==item:
            found=True
        else:
            pos+=1
    return found
def main():
    testlist=[1,2,3,4,55,6,7,9]
    argvlist=sys.argv[1:]
    for i in argvlist:
        print(sequentialSearch(testlist,i))
if __name__=="__main__":
    main()
#./ch11/1.py 1 3 5 7 9 2 4 6 8 10