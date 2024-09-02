import sys
input = sys.stdin.readline

n,m = map(int,input().split())

# 유클리드 호제법, x,y의 최대공약수는 y,r의 최대공약수와 같다.
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

result = gcd(n,m)

# 최소공배수는 두 자연수의 곱 / 최대 공약수


print(result, int(n*m/result))