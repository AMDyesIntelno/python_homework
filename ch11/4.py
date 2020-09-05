#!/usr/bin/python3
import argparse
def merge(left,right):
    merged=[]
    i,j=0,0
    left_len,right_len=len(left),len(right)
    while i<left_len and j<right_len:
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def mergesort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=mergesort(array[:mid])
    right=mergesort(array[mid:])
    return merge(left,right)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--list",type=int,nargs='+')
    args=parser.parse_args()
    list=args.list
    print(mergesort(list))
if __name__ == "__main__":
    main()
#./ch11/4.py --list 10 9 8 7 6 5 4 3 2 1