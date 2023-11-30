def solution(n, lost, reserve):
    # 여벌이 있는데, 체육복을 도난당한 경우 처리
    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)

    result = n
    reserve_info_list = []
    
    # 여분이 있는 학생에 대해 이전번호 혹은 이후번호 학생 중 도난당한 학생이 양쪽 다인지 확인
    for reserve_student in reserve:
        if reserve_student - 1 in lost and reserve_student + 1 in lost:
            reserve_info_list.append([reserve_student, 2])
        elif reserve_student - 1 in lost or reserve_student + 1 in lost:
            reserve_info_list.append([reserve_student, 1])
    # 여분이 있는 학생의 이전/이후 중 한쪽만 도난당한 경우를 우선적으로 정렬
    reserve_info_list.sort(key = lambda x : x[1])
    # 반복문을 통해 체육복을 빌려줌
    for reserve_info in reserve_info_list:
        if reserve_info[0] -1 in lost:
            lost.remove(reserve_info[0] - 1)
        elif reserve_info[0] + 1 in lost:
            lost.remove(reserve_info[0] + 1)
    # 체육복을 빌리지 못한 학생을 제외시킴
    result -= len(lost)
    return result