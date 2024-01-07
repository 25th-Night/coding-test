def dfs(graph, visited, start):
    cnt = 1
    stack = [start]
    visited[start] = True
    while stack:
        v = stack.pop()
        for n in graph[v]:
            if not visited[n]:
                stack.append(n)
                visited[n] = True
                cnt += 1
    return cnt

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

result = []

for x in range(1, n+1):
    visited = [False] * (n+1)
    result.append((x, dfs(graph, visited, x)))

max_ = max(result, key=lambda x:x[1])[1]

print(*[n for n, c in result if c == max_])