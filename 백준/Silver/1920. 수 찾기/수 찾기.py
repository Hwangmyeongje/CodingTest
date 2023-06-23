import sys
input = sys.stdin.readline
n = int(input())
#set로 중복된 수 제거
a= set(map(int,input().split()))
m = int(input())
b =list(map(int,input().split()))
for num in b:
    print(1) if num in a else print(0)