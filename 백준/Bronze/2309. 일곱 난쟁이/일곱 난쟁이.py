import sys
input = sys.stdin.readline
seven = []
for i in range(9):
    seven.append(int(input()))
sum_s = sum(seven)
rm1=0
rm2=0
for i in range(8):
    for j in range(i+1,9):
        if sum_s - seven[i] - seven[j] == 100:
            rm1 = seven[i]
            rm2 = seven[j]
seven.remove(rm1)
seven.remove(rm2)
seven.sort()
# unpacking한 데이터로 전달해야 sep 적용 가능
print(*seven,sep="\n")
