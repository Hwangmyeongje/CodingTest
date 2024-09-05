t = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


for i in range(t):
    arr = list(map(int,input().split()))
    n = arr[0]
    arr = arr[1:]
    gcd_sum = 0
    for a in range(n):
        for b in range(a+1,n):
            gcd_sum += gcd(arr[a],arr[b])
    print(gcd_sum)




