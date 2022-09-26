def solution(s):
    # cnt : 이진 변환의 횟수
    cnt = 0
    # num : 제거된 0의 개수
    num = 0
    # s가 "1"이 될 때까지 실행을 반복
    while s != "1":
        # 제거할 0의 개수를 계산하여 num에 추가
        num += s.count("0")
        # 1의 개수만 계산
        s = s.count("1")
        # s의 길이를 계산하여 2진수로 변환
        s = bin(s)[2:]
        # 모든 변환이 완료된 후, 변환 횟수를 +1
        cnt += 1
    return [cnt, num]