import sys
input = sys.stdin.readline
#시계 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def cleaning(n,m):
    graph = []
    cnt = 0
    r,c,d= map(int,input().split())
    for i in range(n):
        graph.append(list(map(int,input().split())))
    cnt += 1
    #방문한 곳은 2로 바꿈
    graph[r][c] =2
    while(1):
        flag = 0
        #왼쪽 방향으로 돌려야함
        for _ in range(4):
            #반시계 방향으로 돌릴 수 있음 3-> 2 -> 1-> 0
            d = (d+3)%4
            nx = r + dx[d]
            ny = c + dy[d]
            if graph[nx][ny] == 0 and 0<= nx<n and 0<=ny<m:
                r = nx
                c = ny
                cnt +=1
                graph[r][c] = 2
                flag =1
                break
        #flag = 0이면 청소를 못한거다
        if flag == 0:
            if graph[r-dx[d]][c-dy[d]] == 1:
                print(cnt)
                break
            else:
                r = r-dx[d]
                c = c-dy[d]





# 0인 경우 북쪽, 1인  경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽
n,m =map(int,input().split())
cleaning(n,m)



