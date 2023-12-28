def solution(bandage, health, attacks):
    cast, recover, bonus = bandage
    attacks.sort(key=lambda x:x[0])
    result = health
    current = 0
    for i, (time, attack) in enumerate(attacks):
        if i:
            result = min(health, result + recover*(time - current - 1))
            result = min(health, result + bonus *((time-current-1)//cast))
        if result - attack <= 0:
            return -1
        result -= attack
        current = time
    return result