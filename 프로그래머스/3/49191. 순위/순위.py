def solution(n, results):
    inf = float("inf")
    graph = [[inf] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        graph[i][i] = 0
        
    for w, l in results:
        graph[w][l] = 1
        graph[l][w] = -1
        
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == graph[k][b] == 1:
                    graph[a][b] = 1
                elif graph[a][k] == graph[k][b] == -1:
                    graph[a][b] = -1
    answer = 0
    for row in graph:
        if row.count(1) + row.count(-1) == n-1:
            answer += 1
    return answer