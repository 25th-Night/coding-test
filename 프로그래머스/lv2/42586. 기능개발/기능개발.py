from math import ceil

def solution(progresses, speeds):
    day_required = []
    
    for p, s in zip(progresses, speeds):
        day_required.append(ceil((100-p)/s))
    day_required.append(max(day_required)+1)
    print(f"day_required = {day_required}")
    
    temp = []
    answer = []
    
    for i in range(len(day_required)-1):
        if max(day_required[:i+1]) < day_required[i+1]:
            temp.append(day_required[i])
            answer.append(len(temp))
            temp.clear()
            
        else:
            temp.append(day_required[i])
            
    print(f"answer = {answer}")
    return answer