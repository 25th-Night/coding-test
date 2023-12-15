def solution(arr):
    num_cnt = len(arr) // 2 + 1
    nums = [int(num) for num in arr[::2]]
    ops = [op for op in arr[1::2]]
    dp_M = [[-float("inf")] * num_cnt for _ in range(num_cnt)]
    dp_m = [[float("inf")] * num_cnt for _ in range(num_cnt)]
    for i in range(num_cnt):
        dp_M[i][i] = dp_m[i][i] = nums[i]

    for length in range(1, num_cnt):
        for i in range(num_cnt - length):
            j = i + length
            for k in range(i, j):
                if ops[k] == "+":
                    dp_M[i][j] = max(dp_M[i][j], dp_M[i][k] + dp_M[k+1][j])
                    dp_m[i][j] = min(dp_m[i][j], dp_m[i][k] + dp_m[k+1][j])
                elif ops[k] == "-":
                    dp_M[i][j] = max(dp_M[i][j], dp_M[i][k] - dp_m[k+1][j])
                    dp_m[i][j] = min(dp_m[i][j], dp_m[i][k] - dp_M[k+1][j])
            
    return dp_M[0][-1]
