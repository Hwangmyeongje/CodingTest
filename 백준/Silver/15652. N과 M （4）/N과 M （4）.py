import sys
input = sys.stdin.readline
n,m = map(int,input().split())

#1부터 n까지 자연수 중 M개를 고른 수열

#같은 수 골라도 됨

seq = []

def dfs(start):
    if len(seq) == m:
        return print(' '.join(map(str,seq)))
    for i in range(start,n+1):
        seq.append(i)
        dfs(i)
        seq.pop()
dfs(1)