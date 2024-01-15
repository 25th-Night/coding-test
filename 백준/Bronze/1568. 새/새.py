N = int(input())
t = 0
k = 0
while N:
    t += 1
    k += 1
    if N < k:
        k = 1
    N -= k

print(t)
