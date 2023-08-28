cal = input().split('-')
a = [] # -로 나눈 항들 저장
for i in cal:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    a.append(sum)
n = a[0]

for i in range(1,len(a)):
    n -= a[i]
print(n)