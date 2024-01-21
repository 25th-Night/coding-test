def check(row, x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        elif abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(row, x, n):
    result = 0
    if x == n:
        return 1
    for i in range(n):
        row[x] = i
        if check(row, x):
            result += dfs(row, x+1, n)
    return result

n = int(input())
row = [0] * n
result = dfs(row, 0, n)
print(result)