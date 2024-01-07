N, K = map(int, input().split())

visited = [0] * 100001

q = [N]
while q:
    v = q.pop(0)
    if v == K:
        print(visited[v])
        break
    for n in (v-1, v+1, 2*v):
        if n in range(100001) and not visited[n]:
            visited[n] = visited[v] + 1
            q.append(n)