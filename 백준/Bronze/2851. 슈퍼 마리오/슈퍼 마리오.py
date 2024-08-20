import sys
input = sys.stdin.readline
mario = []
temp_sum = 0
pre = []
for i in range(10):
    mario.append(int(input()))
    temp_sum += mario[i]
    pre.append(temp_sum)

index = 9
for i in range(10):
    if pre[i] > 100:
        index = i
        if (pre[i] - 100) > (100 - pre[i-1]):
            index = i-1
        break
print(pre[index])