from collections import Counter

def solution(nums):
    count = Counter(nums)
    sort_num = len(list(count.keys()))
    extract_monsters_num = len(nums) // 2
    return min(sort_num, extract_monsters_num)