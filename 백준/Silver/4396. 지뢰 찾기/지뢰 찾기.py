import sys
input = sys.stdin.readline

n = int(input())
landmine = []
for i in range(n):
    landmine.append(input().strip())
open_section = []
for i in range(n):
    open_section.append(input().strip())

nearby_landmine = [['.'] * n for _ in range(n)]
# 상,좌상,우상,하,좌하,우하,우,좌
dx = [0,-1,1,0,-1,1,1,-1]
dy = [1,1,1,-1,-1,-1,0,0]

game_over = False

for x in range(n):
    for y in range(n):
        cnt = 0
        if open_section[x][y] != 'x':
            continue
        else:
            if landmine[x][y] == '*':
                game_over = 'True'
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if(nx>=0 and ny >= 0 and ny<n and nx<n):
                    if landmine[nx][ny] == '*':
                        cnt +=1
            nearby_landmine[x][y] = cnt
if game_over:
    for x in range(n):
        for y in range(n):
            if landmine[x][y] == '*':
                nearby_landmine[x][y] = '*'

for row in nearby_landmine:
    print("".join(map(str,row)))

# for row in nearby_landmine:
#     for i in row:
#         print(i,end='')
#     print()

