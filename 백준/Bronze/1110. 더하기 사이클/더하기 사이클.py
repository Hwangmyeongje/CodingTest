n = int(input())
if n < 10:
    n *= 10
k = n
cnt = 0
while(1):
    cnt +=1
    num1 = k%10
    num2 = k // 10
    num3 = num1 + num2
    k = (num1 * 10) + (num3 %10)
    if k == n:
        print(cnt)
        break




