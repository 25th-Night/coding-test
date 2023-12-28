def solution(price, money, count):
    return max(count*(2*price + (count-1)*price)//2 - money, 0)