def solution(a, b):
    days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    after_days = 0
    for i in range(1,a):
        after_days += days[i]
    after_days += b - 1
    day_idx = after_days % 7
    day_info = {0:"FRI", 1:"SAT", 2:"SUN" ,3:"MON", 4:"TUE", 5:"WED", 6:"THU"}
    return day_info[day_idx]