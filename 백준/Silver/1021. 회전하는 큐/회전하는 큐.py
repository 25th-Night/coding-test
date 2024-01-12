from collections import deque

N, M = map(int, input().split(" "))
arr = map(int, input().split(" "))
seq = deque(range(1, N+1))
total = 0
for n in arr:
    if seq[0] != n:
        left = seq.index(n)
        right = len(seq) - left
        if left < right:
            total += left
            seq.rotate(-1 * left)
        else:
            total += right
            seq.rotate(right)
    seq.popleft()
print(total)