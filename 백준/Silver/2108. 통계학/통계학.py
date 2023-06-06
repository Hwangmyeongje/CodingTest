from collections import Counter
def modefinder(arr):
    cnt = Counter(arr)
    order = cnt.most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes
n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))

#산술평균
print(round(sum(arr)/n))
arr.sort()
#중앙값
print(arr[n//2])
mode_list= modefinder(arr)
#최빈값 중 두 번째로 작은 값
if len(mode_list)>1:
    print(mode_list[1])
else:
    print(mode_list[0])
range_val = max(arr) - min(arr)
#범위
print(range_val)
