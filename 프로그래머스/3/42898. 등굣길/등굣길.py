def solution(m, n, puddles):
    map = [[1 for j in range(m)] for i in range(n)]

    # 상단, 좌측 라인의 경우, 우물부터 끝까지 좌표값을 0으로 변경
    for x, y in puddles:
        if x == 1:
            for i in range(y-1, n):
                map[i][x-1] = 0
        if y == 1:
            for i in range(x-1, m):
                map[y-1][i] = 0

    # 우물 좌표값을 0으로 변경
    for x, y in puddles:
        map[y-1][x-1] = 0

    for x in range(m):
        for y in range(n):
            # 범위 벗어나는 경우
            if x-1 < 0 or y-1 < 0:
                continue
            # 우물은 건너뛰기
            if map[y][x] == 0:
                continue
            # 해당 좌표값은 좌측 좌표와 상단 좌표의 좌표값의 합
            map[y][x] = map[y][x-1] + map[y-1][x]

    return map[n-1][m-1] % 1000000007