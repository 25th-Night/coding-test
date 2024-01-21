from collections import defaultdict, deque

def bfs(graph, visited, s, e):
    q = deque([(s, 0)])
    visited[s] = True
    while q:
        cn, cd = q.popleft()
        if cn == e:
            return cd
        for nn in graph[cn]:
            if not visited[nn]:
                visited[nn] = True
                q.append((nn, cd + graph[cn][nn]))

N, M = map(int, input().split())
graph = defaultdict(dict)
for _ in range(N-1):
    x, y, d = map(int, input().split())
    graph[x][y]=d
    graph[y][x]=d
result = [0]* M

for i in range(M):
    s, e = map(int, input().split())
    visited= [False] * (N+1)
    print(bfs(graph, visited, s, e))
