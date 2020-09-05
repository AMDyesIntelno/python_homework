#!/usr/bin/python3
import argparse
def selectionsort(array):
    for i in range(0,len(array)):
        posi=i
        for j in range(i+1,len(array)):
            if array[j]<array[posi]:
                posi=j

        array[posi],array[i]=array[i],array[posi]
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--list",type=int,nargs='+')
    args=parser.parse_args()
    list=args.list
    selectionsort(list)
    print(list)
if __name__ == "__main__":
    main()
#./ch11/3.py --list 10 9 8 7 6 5 4 3 2 1