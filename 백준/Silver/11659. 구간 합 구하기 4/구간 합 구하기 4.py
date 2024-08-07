import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr= list(map(int,input().split()))
pre_sum =[0]
temp = 0
for i in arr:
    temp += i
    pre_sum.append(temp)
for i in range(m):
    x,y = map(int,input().split())
    print(pre_sum[y]-pre_sum[x-1])