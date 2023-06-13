import sys
input = sys.stdin.readline
r,c,t = map(int,input().split())
graph =[]
for _ in range(r):
    graph.append(list(map(int,input().split())))

up = 0
down =0
for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i+1
        break
#미세먼지 확산 부분
def spread():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    #동시에 확산이 이루어지는 경우에 대한 문제 해결 위한 변수
    spread_graph = [[0]* c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                cnt = 0
                for k in range(4): #4방향 확인
                    nx = i +dx[k]
                    ny = j + dy[k]
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny] != -1:
                        spread_graph[nx][ny] += graph[i][j] // 5
                        cnt +=1
                graph[i][j] -= (graph[i][j]//5) *cnt
    for i in range(r):
        for j in range(c):
            graph[i][j] += spread_graph[i][j] #확산된 결과를 더해준다.

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)


