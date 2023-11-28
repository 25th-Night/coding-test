def solution(answers):
    check1 = [1, 2, 3, 4, 5]
    check2 = [2, 1, 2, 3, 2, 4, 2, 5]
    check3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct1 = [x for idx, x in enumerate(answers) if x == check1[idx%len(check1)] ]    
    correct2 = [x for idx, x in enumerate(answers) if x == check2[idx%len(check2)] ]    
    correct3 = [x for idx, x in enumerate(answers) if x == check3[idx%len(check3)] ]
    answers_list = [len(correct1), len(correct2), len(correct3)]
    
    max_ = max(answers_list)
    result = []
    for i, c in enumerate([len(correct1), len(correct2), len(correct3)], start=1):
        if c == max_:
            result.append(i)
    return result