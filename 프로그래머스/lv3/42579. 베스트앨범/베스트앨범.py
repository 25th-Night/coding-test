def solution(genres, plays):
    
    # dic1 → '장르 : 재생곡 합계" 를 담은 dict 형식으로 만듦
    length = len(genres)
    dic1 = {}
    for i in range(length):
        dic1[genres[i]] = dic1.get(genres[i], 0) + plays[i]
    print(dic1)

    # dic2 → '장르 : (재생곡, 재생곡의 idx)' 형태의 tuple을 담은 dict로 만듦.
    dic2 = {j:[] for j in genres}
    for k in range(length):
        dic2[genres[k]].append([plays[k],k])
    print(dic2)

    # dic3 → '장르별 재생곡 합계 : (재생곡, 재생곡의 idx)' 형태의 tuple을 담은 dict로 만듦
    length2 = len(dic2)
    dic3 = {l:[] for l in dic1.values()}
    for i in range(length2):
        dic3[list(dic1.values())[i]] = dic3.get(list(dic1.values())[i], 0) + list(dic2.values())[i]
    # dic3 → 위에서 만든 dict를 '장르별 재생곡 합계'를 기준으로 역순 정렬
    dic3 = sorted(dic3.items(), key=lambda x: x[0], reverse=True)
    print(dic3)


    result = []
    for i in dic3:
        # 한 장르 내에서 재생횟수는 역순으로, 동일 재생횟수에 대해서는 idx를 순서대로 정렬
        arr = sorted(i[1], key=lambda x: (-x[0],x[1]))
        print(arr)
        # 한 장르 내에 곡이 하나라면 그것만 추가
        if len(arr) == 1:
            result.append(arr[0][1])
        # 한 장르 내에 곡이 2개 이상이라면 2개까지만 추가
        else:
            for j in range(2):
                result.append(arr[j][1])
    return result