import heapq
import sys
n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card,int(sys.stdin.readline()))
if len(card) == 1:
    print(0)
else:
    cnt = 0
    while len(card) >1:
        temp1 = heapq.heappop(card)
        temp2 = heapq.heappop(card)
        temp3 = temp1+temp2
        cnt += temp3
        heapq.heappush(card,temp3)
    print(cnt)
