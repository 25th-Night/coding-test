def solution(routes):
    routes.sort(key = lambda x : (x[1], x[0]))
    
    result = 0
    idx = 0
    
    while idx < len(routes):
        camera = routes[idx][1]
        idx += 1
        while idx < len(routes) and routes[idx][0] <= camera <= routes[idx][1]:
            idx += 1
        result += 1

    return result