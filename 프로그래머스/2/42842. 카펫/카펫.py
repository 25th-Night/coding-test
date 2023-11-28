def solution(brown, yellow):
    total_cnt = brown + yellow
    for i in range(total_cnt // 2, int(total_cnt**0.5) - 1, -1):
        if not total_cnt % i:
            width, height = i, total_cnt // i
            if (width - 2)*(height - 2) == yellow:
                return [width, height]