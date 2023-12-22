def check(w1, w2):
    d = 0
    for c1, c2 in zip(w1, w2):
        d += c1 != c2
    return d == 1

def dfs(c, t, words, visited, depth):
    if c == t:
        return depth
    min_depth = float("inf")
    for i, w in enumerate(words):
        if check(c, w) and not visited[i]:
            visited[i] = True
            min_depth = min(min_depth, dfs(w, t, words, visited, depth+1))
            visited[i] = False
    return min_depth

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)
    return dfs(begin, target, words, visited, 0)