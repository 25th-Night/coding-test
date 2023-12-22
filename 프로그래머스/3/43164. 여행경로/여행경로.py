from collections import defaultdict

def make_graph(tickets):
    g = defaultdict(list)
    for s, e in tickets:
        g[s].append(e)
    for k in g:
        g[k].sort()
    return g

def solution(tickets):
    graph = make_graph(tickets)
    
    stack = ["ICN"]
    path = []
    
    while stack:
        current = stack[-1]
        if graph[current]:
            stack.append(graph[current].pop(0))
        else:
            path.append(stack.pop())
    return path[::-1]

def solution(tickets):
    graph = make_graph(tickets)
    
    stack = ["ICN"]
    unreturn = []
    
    while stack:
        current = stack[-1]
        if current not in graph or not graph[current]:
            unreturn.append(stack.pop())
        else:
            stack.append(graph[current].pop(0))
            
    if unreturn:
        return unreturn[::-1]
    
    return stack