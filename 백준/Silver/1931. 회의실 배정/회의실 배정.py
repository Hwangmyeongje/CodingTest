n = int(input())
#1. 빨리 끝나는 회의 순서대로 정렬
#2. 끝나는 시간이 같을 경우는 빨리 시작하는 순서대로 정렬
time = []
for _ in range(n):
    start,end = map(int,input().split())
    time.append([start,end])
time = sorted(time, key = lambda a : a[0]) # start 기준으로 오름차순 정렬
time = sorted(time, key = lambda a : a[1]) # end 기준으로 오름차순 정렬

last_end = 0
cnt = 0
for start,end in time:
    if start >= last_end:
        cnt+=1
        last_end = end
print(cnt)

