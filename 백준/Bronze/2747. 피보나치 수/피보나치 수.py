import sys
input = sys.stdin.readline

# 재귀 이용시 시간초과
# def fibo(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# n = int(input())
# print(fibo(n))

n= int(input())
a,b=0,1
for i in range(n):
    a,b= b, a+b
print(a)
