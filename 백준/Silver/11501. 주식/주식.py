T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    check = [0] * N
    check[-1] = m = arr[-1]
    for i in range(N-2, -1, -1):
        if arr[i] > m:
            m = arr[i]
        check[i] = m
    result = 0
    for i in range(N):
        result += check[i] - arr[i]
    print(result)
