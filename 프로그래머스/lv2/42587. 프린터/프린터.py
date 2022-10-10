def solution(priorities, location):
    target = priorities[location]
    print(target)
    while priorities:
        J = priorities[0]
        if J < max(priorities[1:]):
            J = priorities.pop(0)
            priorities.append(J)
        else:
            break
    print(priorities)
    
    return priorities.index(target)+1