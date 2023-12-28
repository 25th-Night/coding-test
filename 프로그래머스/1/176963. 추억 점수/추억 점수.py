def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    answer = []
    for people in photo:
        total = 0
        for p in people:
            if p in dic:
                total += dic[p]
        answer.append(total)
    return answer