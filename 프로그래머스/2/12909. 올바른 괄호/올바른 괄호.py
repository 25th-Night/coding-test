def solution(s):
    stack = []
    for c in s:
        if (not stack or (stack and stack[-1] == "(")) and c == "(":
            stack.append(c)
        elif stack and stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            return False
    return len(stack) == 0