from itertools import permutations

def check(p,ban):
    if len(p) == len(ban):
        for i,j in zip(p,ban):
            if j == '*':
                continue
            elif i!=j:
                return False
                
    else:
        return False
    return True

def solution(user_id, banned_id):
    answer =[]
    for permu in permutations(user_id,len(banned_id)):
        flag = True
        for i in range(len(banned_id)):
            if not check(permu[i],banned_id[i]):
                flag = False
        if flag:
            if set(permu) not in answer:
                answer.append(set(permu))
    
    return len(answer)