from collections import Counter
n = int(input())
a= list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
count = Counter(a)
for j in b:
    if j in count:
        print(count[j],end=' ')
    else:
        print(0,end=' ')

