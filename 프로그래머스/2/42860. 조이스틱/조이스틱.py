def solution(name):
    answer = 0
    
    # 기본 이동값 : 시작 지점에서 끝까지 우측으로만 이동하는 경우
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # 알파벳별 조이스틱을 상하로 움직이는 횟수 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 현재 알파벳 다음을 기준으로 A가 아닌 요소의 idx를 확인
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 최소로 움직여야 할 거리를 아래 세 개의 값 중 최솟값으로 매번 계산하여 거리 업데이트
        # - 기본 이동값
        # - 시작점에서 i까지 왕복 + 좌측으로 돌아 시작점을 지나쳐 next까지 이동하기 (▶ - ◀ - ▶)
        # - 시작점에서 next까지 왕복 + 우측으로 돌아 시작점을 지나쳐 i까지 이동하기 (◀ - ▶ - ◀)
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    answer += min_move
    return answer