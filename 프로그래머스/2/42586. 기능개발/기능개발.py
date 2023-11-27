def solution(progresses, speeds):
    answer = []
    deploy_list = []
    for progress, speed in zip(progresses, speeds):
        if int((100-progress) / speed) == (100-progress) / speed:
            deploy_list.append((100-progress) / speed)
        else:
            deploy_list.append(((100-progress) // speed)+1)
    
    last, cnt = 0, 0
    
    for deploy in deploy_list:
        if last and deploy > last:
            answer.append(cnt+1)
            last, cnt = deploy, 0
        elif last and deploy <= last:
            
            cnt += 1
        else:
            last = max(last, deploy)
    if last:
        answer.append(cnt+1)
    
    return answer
