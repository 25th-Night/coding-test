def solution(targets):
    answer = 0
    targets.sort(key = lambda x:(x[1], x[0]))
    
    e = 0
    for cs, ce in targets:
        if cs >= e:
            answer += 1
            e = ce

    return answer