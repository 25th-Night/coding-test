def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    b1 = sum(1 for i, a in enumerate(answers) if a1[i%5] == a)
    b2 = sum(1 for i, a in enumerate(answers) if a2[i%8] == a)
    b3 = sum(1 for i, a in enumerate(answers) if a3[i%10] == a)
    
    result = map(lambda x: x[0], (filter(lambda x: x[1] == max(b1, b2, b3), enumerate([b1, b2, b3], start=1))))
    return list(result)