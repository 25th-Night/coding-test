from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(set(arr))

check = defaultdict(int)

for i, n in enumerate(arr2):
    check[n] = i

for x in arr:
    print(check[x], end=" ")