def solution(park, routes):
    answer = []
    for r in range(len(park)):
        if "S" in park[r]:
            cr, cc = r, park[r].index("S")
            break
    move = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    for route in routes:
        direction, nums = route.split(" ")
        r, c = move[direction]
        if cr+r*int(nums) not in range(len(park)) or cc+c*int(nums) not in range(len(park[0])):
            continue
        stop = False
        for num in range(1, int(nums)+1):
            nr, nc = cr+r*num, cc+c*num
            print(nr, nc, park[nr][nc])
            if park[nr][nc] == "X":
                stop = True
                break
        if not stop:
            cr, cc = cr+r*int(nums), cc+c*int(nums)
    return [cr, cc]