def solution(n, arr1, arr2):
    dp1, dp2 = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
    for r, num in enumerate(arr1):
        trans_num = bin(num)[2:] if len(bin(num)[2:]) == n else "0" * (n-len(bin(num)[2:])) + bin(num)[2:]
        for i, n1 in enumerate(trans_num):
            dp1[r][i] = int(n1)
    for r, num in enumerate(arr2):
        trans_num = bin(num)[2:] if len(bin(num)[2:]) == n else "0" * (n-len(bin(num)[2:])) + bin(num)[2:]
        for i, n2 in enumerate(trans_num):
            dp2[r][i] = int(n2)
    result = []
    for r in range(n):
        temp = ""
        for c in range(n):
            temp += "#" if dp1[r][c] + dp2[r][c] else " "
        result.append(temp) 
    return result