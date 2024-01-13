from heapq import heappop, heappush
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M = int(input())
    arr = []
    for _ in range(M//10 + 1):
        arr += list(map(int, input().split()))
    left, median, right = [], arr[0], []
    result = [median]
    for i, n in enumerate(arr[1:], 1):
        if n <= median:
            heappush(left, -n)
        else:
            heappush(right, n)
        if not i % 2:
            if len(left) > len(right):
                heappush(right, median)
                median = -heappop(left)
            elif len(left) < len(right):
                heappush(left, -median)
                median = heappop(right)
            result.append(median)
    
    print(len(result))
    for i, n in enumerate(result, 1):
        print(n, end=" ")
        if not i%10:
            print()
