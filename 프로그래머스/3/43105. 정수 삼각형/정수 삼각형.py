def solution(triangle):
    dp = [[0] * i for i in range(1, len(triangle)+ 1)]
    for i, floor in enumerate(triangle):
        for j, value in enumerate(floor):
            if not (i + j) :
                dp[i][j] = value
            else:
                if j == 0:
                    dp[i][j] = value + dp[i-1][j]
                elif j == len(floor) - 1:
                    dp[i][j] = value + dp[i-1][j-1]
                else:
                    dp[i][j] = value + max(dp[i-1][j-1], dp[i-1][j])
    answer = max(dp[-1])
    return answer