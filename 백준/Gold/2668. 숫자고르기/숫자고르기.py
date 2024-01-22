import sys

sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline


def dfs(s, graph, visited, group, result):
    visited[s] = True
    group.append(s)
    n = graph[s]
    
    if not visited[n]:
        dfs(n, graph, visited, group, result)
    else:
        if n in group:
            result += group[group.index(n):]

N = int(input())
graph = [0] + [int(input()) for _ in range(N)]
visited = [False] * (N+1)
result = []

for i in range(1, N+1):
    if not visited[i]:
        group = []
        dfs(i, graph, visited, group, result)

result.sort()
print(len(result))
print("\n".join(map(str, result)))