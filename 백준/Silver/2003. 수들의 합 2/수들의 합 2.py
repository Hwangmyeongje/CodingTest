import sys
input = sys.stdin.readline

n,m = map(int,input().split())

A = list(map(int,input().split()))

sum = A[0]
left = 0
right = 1
cnt = 0


while (right<=n):
    #현재 부분합이 목표값 m보다 작다면, right 포인터를 이동해 범위를 넓힘
    if sum < m:
        if right == n: #right가 배열의 끝에 도달했으므로 루프 종료
            break
        sum += A[right]
        right +=1
    elif sum == m:
        #현재 부분합이 목표값 m과 같으니 카운트 증가시키고 left 포인터를 이동시켜 버뮈를 좁힘
        cnt +=1
        sum -= A[left]
        left += 1
    elif sum > m:
        #현재 부분합이 목표값 m보다 크므로 left 포인터 이동시켜 범위를 좁힌다.
        sum -= A[left]
        left += 1

print(cnt)

