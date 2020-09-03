#!/usr/bin/python3
import sys
n=int(sys.argv[1])
with open("./out.log","w") as f:
    sys.stdout=f
    print(str([i for i in range(0,n+1)]))
    print(str([i*2 for i in range(0,n+1)]))
    print(str([2**i for i in range(0,n+1)]),end="")