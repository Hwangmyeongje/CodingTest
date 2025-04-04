from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

deq = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            deq.append((i,j))
# 좌상 우상 상 좌하 우하 하 좌 우
dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,1,0,-1,1,0,-1,1]


def bfs():
    while deq:
        x,y = deq.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] +1
                    deq.append((nx,ny))

bfs()

maxnum = 0
for i in range(n):
    for j in range(m):
        maxnum = max(maxnum,arr[i][j])

print(maxnum - 1)
