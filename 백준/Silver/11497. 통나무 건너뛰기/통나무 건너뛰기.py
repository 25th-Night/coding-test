import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    max_diff = 0
    for i in range(n - 2):
        diff = abs(arr[i] - arr[i + 2])
        max_diff = max(max_diff, diff)
    print(max_diff)