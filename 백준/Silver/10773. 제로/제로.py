from collections import deque
k = int(input())
deq = deque()
for i in range(k):
    n = int(input())
    if n != 0:
        deq.append(n)
    else:
        if(len(deq) > 0):
            deq.pop()
print(sum(deq))
