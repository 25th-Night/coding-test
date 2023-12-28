def solution(ingredient):
    stack = []
    cnt = 0
    for f in ingredient:
        if len(stack) >= 3 and stack[-3:] + [f] == [1,2,3,1]:
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1
        else:
            stack.append(f)
    return cnt