#!/usr/bin/python3
import argparse
def quicksort(array,start,end):
    if start>=end:
        return
    left,right=start,end
    mid=array[(left+right)//2]
    while left<right:
        while array[left]<mid:
            left+=1
        while array[right]>mid:
            right-=1
        if left<=right:
            array[left],array[right]=array[right],array[left]
            left+=1
            right-=1
    quicksort(array,start,right)
    quicksort(array,left,end)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--list",type=int,nargs='+')
    args=parser.parse_args()
    list=args.list
    quicksort(list,0,len(list)-1)
    print(list)
if __name__ == "__main__":
    main()
#./ch11/5.py --list 10 9 8 7 6 5 4 3 2 1