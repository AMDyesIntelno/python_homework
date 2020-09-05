#!/usr/bin/python3
import argparse
def binarySearch(l,item):
    start=0
    end=len(l)-1
    while start<=end:
        mid=(start+end)//2
        if l[mid]<item:
            start=mid+1
        elif l[mid]>item:
            end=mid-1
        else:
            return mid
    return -1
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--list",type=int,nargs='+')
    parser.add_argument("--find",type=int,nargs='+')
    args=parser.parse_args()
    list=args.list
    find=args.find
    for i in find:
        print("关键字位于列表索引%d"%binarySearch(list,i))
if __name__ == "__main__":
    main()
#./ch11/2.py --list 1 2 3 4 5 7 8 9 10 --find 1 2 3 5 9 11