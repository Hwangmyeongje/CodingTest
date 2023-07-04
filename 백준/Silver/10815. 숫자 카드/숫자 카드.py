n= int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
#이진 탐색을 위해서 정렬을 시켜줌
a.sort()
def binary_search(arr,target,start,end):
    while start <=end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None
for i in range(m):
    if binary_search(a,b[i],0,n-1) is not None:
        print(1,end=' ')
    else:
        print(0,end=' ')