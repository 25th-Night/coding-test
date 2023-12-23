def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    cnt = 0
    while left <= right:
        current = people[right]
        cnt += 1
        right -= 1
        if current + people[left] <= limit:
            left += 1
    return cnt