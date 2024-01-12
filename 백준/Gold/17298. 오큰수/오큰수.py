import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

index = []
NGE = [-1] * N

for i, n in enumerate(arr):
    while index and arr[index[-1]] < n:
        NGE[index[-1]] = n
        index.pop()
    index.append(i)

print(*NGE)