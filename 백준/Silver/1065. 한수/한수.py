# N보다 작거나 같은 한수의 개수
def hansu(n):
    cnt = 99
    if(n<100):
        print(n)
    elif n>=100:
        for i in range(100,n+1):
            n1 =  i%10
            n2 = (i//10) %10
            n3 = (i//100)
            if n3 - n2 == n2 - n1:
                cnt+=1
        print(cnt)


n = int(input())
hansu(n)