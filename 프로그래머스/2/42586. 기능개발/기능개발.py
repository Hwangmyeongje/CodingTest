def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(progresses)):
        y = 0
        x = 100 - progresses[i]
        if x % speeds[i] != 0:
            y +=1
        y += x // speeds[i]
        queue.append(y)
    print(queue)
    temp = queue.pop(0)
    cnt = 1
    

    while(queue):
        print(queue)
        if temp >= queue[0]:
            cnt +=1 
            queue.pop(0)
        else:
            answer.append(cnt)
            cnt = 1
            temp = queue.pop(0)
    answer.append(cnt)
        
    
        
        
        
    return answer