def solution(prices):
    dp = [0] * len(prices)
    stack = []
    for i, p in enumerate(prices):
        while stack and stack[-1][-1] > p:
            j, _ = stack.pop()
            dp[j] = i-j
        stack.append((i, p))
    if stack:
        for i, p in stack:
            dp[i] = len(prices) - 1 - i
    return dp