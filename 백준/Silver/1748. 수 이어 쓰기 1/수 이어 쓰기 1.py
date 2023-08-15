n= input()
n_len = len(n) -1
cnt = 0
for i in range(n_len):
    cnt += 9 *(10**i) * (i+1)
    i +=1
cnt += ((int(n)- (10 **n_len))+1)*(n_len+1)
print(cnt)

