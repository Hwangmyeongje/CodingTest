n,k = map(int,input().split())
arr =[]
josephus=[]
for i in range(1,n+1):
    arr.append(i)
#삭제될 인덱스
cnt =0
for i in range(n):
    cnt += k-1
    if cnt>=len(arr):
        cnt = cnt%len(arr)
    josephus.append(arr.pop(cnt))
print("<",end="")
for i in range(n-1):
    print(josephus[i], end=', ')
print(josephus[n-1],end='')
print(">",end="")



