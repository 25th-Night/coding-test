def sum_serial(serial):
    cnt = 0
    for c in serial:
        if c.isdigit():
            cnt += int(c)
    return cnt

N = int(input())
serials = [input() for _ in range(N)]
serials.sort(key=lambda x:(len(x), sum_serial(x), x))

print("\n".join(serials))
