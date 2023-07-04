from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    flag =0
    oper = input().strip()
    n = int(input())
    arr = input().strip()
    #첫 번째 요소와 마지막 요소 제거
    queue = deque(arr[1:-1].split(','))
    rcnt = 0
    #길이가 0인 경우 큐를 빈상태로 초기화한다.
    if n == 0:
        queue= deque()

    for i in oper:
        if i == 'R':
            rcnt +=1
        elif i == 'D':
            if queue:
                if rcnt %2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print("error")
                flag = 1
                break
    if flag == 0:
        if rcnt %2 == 1:
            queue.reverse()
        print('['+",".join(queue)+']')
        