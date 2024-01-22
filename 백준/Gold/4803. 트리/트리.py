import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline

def is_cycle(s, prev):
    visited[s] = True
    for n in graph[s]:
        if not visited[n]:
            if is_cycle(n, s):
                return True
        else:
            if n != prev:
                return True
    return False

test_case = 1
while True:
    n, m = map(int, input().split())
    if not n:
        break
    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n+1)
    
    cnt = 0
    for i in range(1, n+1):
        if not visited[i] and not is_cycle(i, 0):
            cnt += 1
    
    if cnt == 0:
        print(f'Case {test_case}: No trees.')
    elif cnt == 1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {cnt} trees.')
    test_case += 1