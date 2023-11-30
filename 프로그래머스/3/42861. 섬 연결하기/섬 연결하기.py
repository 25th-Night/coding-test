def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    
    return a == b

def solution(n, costs):
    answer = 0
    parent = list(range(n))
    costs.sort(key = lambda x : x[2])

    for node1, node2, cost in costs:
        if get_parent(parent, node1) != get_parent(parent, node2):
            union_parent(parent, node1, node2)
            answer += cost 

    return answer