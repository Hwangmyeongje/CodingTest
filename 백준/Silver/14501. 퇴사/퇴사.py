def max_profit(N, t, p):
    dp = [0] * (N + 1)  # 각 날짜별 최대 수익을 저장하기 위한 DP 테이블

    for i in range(N - 1, -1, -1):
        # 현재 날짜에서 상담을 진행할 경우와 진행하지 않을 경우의 수익 비교
        if t[i] + i > N:  # 상담을 마친 날짜가 퇴사일을 초과하는 경우
            dp[i] = dp[i + 1]  # 다음 날짜의 최대 수익과 동일
        else:
            # 현재 상담을 선택하여 i번째 날부터 t[i]일이 지난 이후에 얻을 수 있는 금액과
            # 현재 상담을 선택하지 않고 다음 날로 넘어갔을 때의 최대 수익 중 큰 값을 선택
            dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])

    return dp[0]  # 첫 번째 날짜부터 최대 수익 반환


n = int(input())  # 상담 일수 입력
t = []  # 상담 일정을 저장할 리스트
p = []  # 상담 금액을 저장할 리스트

for _ in range(n):
    a, b = map(int, input().split())  # 각 상담의 기간과 금액 입력
    t.append(a)
    p.append(b)

result = max_profit(n, t, p)
print(result)
