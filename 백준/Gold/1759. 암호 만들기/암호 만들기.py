from itertools import combinations

L, C = map(int, input().split())
chars = input().split()
chars.sort()

vs = ("a", "e", "i", "o", "u")

for p in combinations(chars, L):
    cnt = 0
    for c in p:
        if c in vs:
            cnt += 1
    if 1 <= cnt <= L-2:
        print("".join(p))