import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
arr.sort()
cnt = 0
for i, x in enumerate(arr):
    cnt += abs(i-x)
print(cnt)