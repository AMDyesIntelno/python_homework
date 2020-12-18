def fun(numbers,target):
    length=len(numbers)
    for i in range(len(numbers)):
        start,end=i+1,length-1
        while start<=end:
            mid=(start+end)//2
            if numbers[mid]+numbers[i]==target:
                return i+1,mid+1
            elif numbers[mid]+numbers[i]>target:
                end=mid-1
            else:
                start=mid+1


numbers=eval(input())
target=int(input())
print(fun(numbers,target))