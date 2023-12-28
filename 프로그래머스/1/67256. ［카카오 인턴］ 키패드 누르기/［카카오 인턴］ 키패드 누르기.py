def calc(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def solution(numbers, hand):
    maps = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}
    left, right = (3,0), (3,2)
    answer = ""
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = maps[num]
        elif num in [3, 6, 9]:
            answer += "R"
            right = maps[num]
        elif num in [2, 5, 8, 0]:
            dist_left, dist_right = calc(maps[num],left), calc(maps[num], right)
            if dist_left < dist_right or (dist_left == dist_right and hand == "left"):
                answer += "L"
                left = maps[num]
            elif dist_left > dist_right or (dist_left == dist_right and hand == "right"):
                answer += "R"
                right = maps[num]
    return answer