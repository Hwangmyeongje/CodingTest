import sys
input = sys.stdin.readline
cnt=0
cow_dict = dict()
n = int(input())
for i in range(n):
    cow,direction = map(int,input().split())
    if cow not in cow_dict:
        cow_dict[cow] = direction
    else:
        if cow_dict[cow] != direction:
            cnt+=1
            cow_dict[cow] = direction
print(cnt)

