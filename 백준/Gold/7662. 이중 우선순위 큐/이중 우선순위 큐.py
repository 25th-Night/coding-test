import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def pop(heap, deleted):
    while len(heap) > 0:
        data, idx = heappop(heap)
        if not deleted[idx]:
            deleted[idx] = True
            return data
    return None

for _ in range(int(input())):
    k = int(input())
    heap_m = []
    heap_M = []
    curr = 0
    deleted = [False] * (k+1)
    for i in range(k):
        o, n = input().split()
        if o == "D":
            if n == "-1":
                pop(heap_m, deleted)
            else:
                pop(heap_M, deleted)
        elif o == "I":
            heappush(heap_m, (int(n), curr))
            heappush(heap_M, (-int(n), curr))
            curr += 1
    max_value = pop(heap_M, deleted)
    if max_value is None:
        print("EMPTY")
    else:
        heappush(heap_m, (-max_value, curr))
        print(-max_value, pop(heap_m, deleted))