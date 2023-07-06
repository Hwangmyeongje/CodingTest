n = int(input())
arr= list(map(int,input().split()))
arr.sort()
sum = 0
sum2 = 0
for i in arr:
    sum += i
    sum2 += sum
print(sum2)