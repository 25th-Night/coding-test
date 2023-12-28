def solution(N, stages):
    total = len(stages)
    dp = [0] * (N+2)
    ps = [0] * (N+2)
    fail = [0] * (N+2)
    for s in stages:
        dp[s] += 1
    for i in range(1, N+1):
        total -= dp[i-1]
        ps[i] = total
    for i in range(1, N+1):
        fail[i] = dp[i]/ps[i] if ps[i] else 0
    result = []
    for i, f in enumerate(fail[1:-1], 1):
        result.append((i, f))
    result.sort(key=lambda x:(-x[1], x[0]))
    return [r[0] for r in result]