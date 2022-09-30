def solution(genres, plays):
    length = len(genres)

    dic1 = {}
    for i in range(length):
        dic1[genres[i]] = dic1.get(genres[i], 0) + plays[i]
    print(dic1)

    dic2 = {j:[] for j in genres}
    for k in range(length):
        dic2[genres[k]].append([plays[k],k])
    print(dic2)

    length2 = len(dic2)
    dic3 = {l:[] for l in dic1.values()}
    for i in range(length2):
        dic3[list(dic1.values())[i]] = dic3.get(list(dic1.values())[i], 0) + list(dic2.values())[i]
    dic3 = sorted(dic3.items(), key=lambda x: x[0], reverse=True)
    print(dic3)

    dic4 = []
    for i in dic3:
        arr = sorted(i[1], key=lambda x: (-x[0],x[1]))
        print(arr)
        if len(arr) == 1:
            dic4.append(arr[0][1])
        else:
            for j in range(2):
                dic4.append(arr[j][1])
    return dic4