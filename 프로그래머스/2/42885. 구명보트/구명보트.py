from collections import deque

def solution(people, limit):
    people.sort()
    
    result = 0
    min_ = 0
    max_ = len(people) - 1
    boat = 0
    while min_ <= max_:
        boat += people[max_]
        max_ -= 1
        if boat + people[min_] <= limit:
            min_ += 1
        result += 1
        boat = 0
        
    return result