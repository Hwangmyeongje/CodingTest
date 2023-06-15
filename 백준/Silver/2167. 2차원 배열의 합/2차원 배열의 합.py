import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append( list(map(int,input().split())))
k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    sum =0
    for a in range(i-1,x):
        for b in range(j-1,y):
            sum += arr[a][b]
    print(sum)
