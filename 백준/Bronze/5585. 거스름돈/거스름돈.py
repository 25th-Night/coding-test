rest = 1000 - int(input())

cnt = 0
types = [500, 100, 50, 10, 5, 1]
idx = 0
while rest:
    if rest >= types[idx]:
        q, rest = divmod(rest, types[idx])
        cnt += q
    idx += 1
print(cnt)
