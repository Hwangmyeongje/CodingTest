import sys
input = sys.stdin.readline
# 윤년 = 4의 배수, not 100의 배수 but 400의 배수면 ok

n = int(input())
if n % 4== 0:
    if n % 100 != 0:
        print(1)
    else:
        if n%400==0:
            print(1)
        else:
            print(0)
else:
    print(0)