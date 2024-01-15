import sys

input = sys.stdin.readline

N = int(input())
cds = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0],x[1]))

for cd in cds:
    print(*cd)