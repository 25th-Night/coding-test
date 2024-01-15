import sys
sys.setrecursionlimit(10**3)

N, r, c = map(int,input().split())
size = 2**N

def dfs(row, col, n, value):
    n = n // 2

    if row < n and col < n:
        if n == 1:
            print(value)
            return
        dfs(row, col, n, value)

    elif row < n and col >= n:
        if n == 1:
            print(value + 1)
            return
        dfs(row, col - n, n, value + n ** 2)

    elif row >= n and col < n:
        if n == 1:
            print(value + 2)
            return
        dfs(row - n, col, n, value + n ** 2 * 2)

    elif row >= n and col >= n:
        if n == 1:
            print(value + 3)
            return
        dfs(row - n, col - n, n, value + n ** 2 * 3)

dfs(r,c,size,0)