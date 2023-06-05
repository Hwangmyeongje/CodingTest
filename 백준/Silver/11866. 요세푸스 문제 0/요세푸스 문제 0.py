n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
Josephus =[]
cnt = 0
for i in range(n):
    cnt +=k-1
    if cnt >= len(arr):
        cnt = cnt % len(arr)
    Josephus.append(arr.pop(cnt))
print("<",end='')
for i in range(n-1):
    print(Josephus[i], end = ', ')
print(Josephus[n-1],end='')
print(">",end='')
