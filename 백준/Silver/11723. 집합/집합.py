import sys
input = sys.stdin.readline
m = int(input())
s = set() #빈 집합 생성
for _ in range(m):
    oper = input().split()
    if len(oper) == 1: #단일 명령어라면 len ==1임
        if oper[0] == 'all':
            s =set(range(1,21))
        else:
            #empty인 경우 공집합으로 초기화한다.
            s = set()
    else:#두 개의 인자를 가지는 경우들
        num = int(oper[1])
        if oper[0] == 'add':
            s.add(num)
        elif oper[0] == 'remove':
            s.discard(num)
        elif oper[0] == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif oper[0] == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)