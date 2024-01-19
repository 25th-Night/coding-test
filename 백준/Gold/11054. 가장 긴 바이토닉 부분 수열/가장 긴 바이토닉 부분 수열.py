N = int(input())
arr = list(map(int, input().split()))
rev = arr[::-1]
inc, dec = [1] * N, [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            inc[i] = max(inc[i], inc[j]+1)
        if rev[j] < rev[i]:
            dec[i] = max(dec[i], dec[j]+1)
            
dec.reverse()

print(max(sum(pair)-1 for pair in zip(inc, dec)))