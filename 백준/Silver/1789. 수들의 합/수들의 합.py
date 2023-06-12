s = int(input())
n = 0
cnt = 0
while(1):
    cnt +=1
    n += cnt
    if n >s:
        break
print(cnt-1)

