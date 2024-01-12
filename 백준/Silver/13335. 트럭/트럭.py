from collections import deque

n, w, L = map(int, input().split())
ts = deque(map(int, input().split()))
bs = deque([0] * w)
bw = 0

time = 0

while ts:
    bw -= bs.popleft()

    if bw + ts[0] <= L:
        bw += ts[0]
        bs.append(ts.popleft())
    else:
        bs.append(0)
    time += 1

time += w

print(time)