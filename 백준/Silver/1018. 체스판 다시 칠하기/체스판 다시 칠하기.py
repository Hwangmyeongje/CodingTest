n,m = map(int,input().split())
graph = []
count = []
for _ in range(n):
    graph.append(input())
#n-7로 해서 돌아야 8칸을 만들 수 있는 경우의 수를 다 구할 수 있음
for i in range(n-7):
    for j in range(m-7):
        w_draw =0
        b_draw = 0
        for k in range(i,i+8):
            for l in range(j, j+8):
                #시작 인덱스와 색이 같아야 한다.
                if (k+l) %2 ==0:
                   if graph[k][l] == 'B':
                       w_draw += 1
                   else:
                       b_draw+= 1
                else:
                    if graph[k][l] == 'W':
                        w_draw+=1
                    else:
                        b_draw+=1
        count.append(min(w_draw,b_draw))
print(min(count))

