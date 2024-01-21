from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))
arr2 = set(arr)
arr3 = sorted(enumerate(arr2), key=lambda x:x[1])

check = defaultdict(int)

for i, t in enumerate(arr3):
    check[t[-1]] = i

for x in arr:
    print(check[x], end=" ")