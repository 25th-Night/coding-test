N = int(input())
cs = [tuple(map(int, input().split())) for _ in range(N)]
cs.sort()

total = 0
start, end = -1e9-2, -1e9-1

for x, y in cs:
    if end <= x:
        start, end = x, y
        total += y-x
    else:
        if y > end:
            total += y-end
            end = y

print(total)
