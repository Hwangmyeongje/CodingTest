n,s = map(int,input().split())
#n은 동생 수
#s가 현재위치

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

brother = list(map(int,input().split()))

for i in range(n):
    brother[i] = abs(s-brother[i])
d=brother[0]
for i in range(1,n):
    d = gcd(d,brother[i])
print(d)
