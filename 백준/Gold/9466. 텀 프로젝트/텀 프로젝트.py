import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))

def dfs(s, graph, visited, team, cnt):
    visited[s] = True
    team.append(s)
    n = graph[s]
    
    if not visited[n]:
        return dfs(n, graph, visited, team, cnt)
    else:
        if n in team:
            cnt -= len(team[team.index(n):])
        return cnt

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    cnt = n
    
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            cnt = dfs(i, graph, visited, team, cnt)

    print(cnt)