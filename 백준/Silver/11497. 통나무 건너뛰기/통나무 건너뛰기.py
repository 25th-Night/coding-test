T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(map(int, input().split()), reverse=True)

    ts = []
    for i, n in enumerate(arr):
        if not i%2:
            ts.insert(0, n)
        else:
            ts.append(n)
    
    result = 0
    for i in range(len(ts)-1):
        result = max(result, abs(ts[i]-ts[i+1]))
    print(result)