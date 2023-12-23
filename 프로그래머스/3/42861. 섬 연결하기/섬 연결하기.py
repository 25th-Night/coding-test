def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = get_parent(parent, x)
    b = get_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    parent = list(range(n))
    answer = 0
    for n1, n2, cost in costs:
        if get_parent(parent, n1) != get_parent(parent, n2):
            union_parent(parent, n1, n2)
            answer += cost
    return answer