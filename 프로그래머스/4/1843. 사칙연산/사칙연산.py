def solution(arr):
    cnt = len(arr) // 2 + 1
    nums = [int(n) for n in arr[::2]]
    ops = [o for o in arr[1::2]]
    dpM = [[-float("inf")] * cnt for _ in range(cnt)]
    dpm = [[float("inf")] * cnt for _ in range(cnt)]
    for i in range(cnt):
        dpM[i][i] = dpm[i][i] = nums[i]
    for length in range(1, cnt):
        for i in range(cnt - length):
            j = i + length
            for k in range(i, j):
                if ops[k] == "+":
                    dpM[i][j] = max(dpM[i][j], dpM[i][k] + dpM[k+1][j])
                    dpm[i][j] = min(dpm[i][j], dpm[i][k] + dpm[k+1][j])
                elif ops[k] == "-":
                    dpM[i][j] = max(dpM[i][j], dpM[i][k] - dpm[k+1][j])
                    dpm[i][j] = min(dpm[i][j], dpm[i][k] - dpM[k+1][j])
    return dpM[0][-1]