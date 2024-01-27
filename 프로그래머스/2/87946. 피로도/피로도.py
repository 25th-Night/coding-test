from itertools import permutations

def count_clear_dungeon(k, dungeon_order):
    clear_cnt = 0
    for dungeon in dungeon_order:
        if k >= dungeon[0]:
            clear_cnt += 1
            k -= dungeon[1]
        else:
            return clear_cnt
    return clear_cnt

def solution(k, dungeons):
    dungeons = list(filter(lambda x: x[0] <= k, dungeons))
    clear_cnt_list = [count_clear_dungeon(k, dungeon_order) for dungeon_order in permutations(dungeons, len(dungeons))]
    
    return max(clear_cnt_list)