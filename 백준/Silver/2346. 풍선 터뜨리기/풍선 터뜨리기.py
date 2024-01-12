from collections import deque

N = int(input())

arr = input().split(" ")
arr = deque((i, int(n)) for i, n in enumerate(arr, 1))

result = []
next = 0
while arr:
    arr.rotate(-next)
    idx, next = arr.popleft()
    if next > 0:
        next = next - 1
    elif next < 0:
        next = next
    result.append(str(idx))

print(" ".join(result))