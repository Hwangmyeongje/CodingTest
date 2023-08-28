#보석 개수 n, 가방 k
#보석 무게 m, 가격 v
#가방에 담을 수 있는 무게 c
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)
