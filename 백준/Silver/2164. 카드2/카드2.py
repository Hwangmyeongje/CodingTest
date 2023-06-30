from collections import deque
n= int(input())
queue = deque()
for i in range(n):
    queue.append(n-i)
while 1:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.pop()
    queue.appendleft(queue.pop())

