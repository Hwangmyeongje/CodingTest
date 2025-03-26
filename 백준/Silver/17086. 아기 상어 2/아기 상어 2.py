from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 상 하 좌 우 좌상 우상  좌하 우하
dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,-1,-1,1,1]

shark = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] ==1:
            shark.append((i,j))

def bfs():
    while shark:
        x,y = shark.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] ==0:
                    shark.append((nx,ny))
                    arr[nx][ny] = arr[x][y]+1
bfs()
safe_dist = 0
for i in range(n):
    for j in range(m):
        safe_dist = max(safe_dist,arr[i][j])
print(safe_dist-1)