def solution(arrows):
    move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    v = {(0, 0)}
    e = set()
    x, y = 0, 0
    
    for direction in arrows:
        for i in range(2):
            nx, ny = x + move[direction][0], y + move[direction][1]
            v.add((nx, ny))
            e.add((min((x, y), (nx, ny)), max((x, y), (nx, ny))))
            x, y = nx, ny
            
    return len(e) - len(v) + 1