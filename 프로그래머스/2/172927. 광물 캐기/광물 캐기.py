def solution(picks, minerals):
    minerals = "".join(minerals)
    minerals = minerals.replace("diamond", "d")
    minerals = minerals.replace("iron", "i")
    minerals = minerals.replace("stone", "s")
    
    arr = []
    
    while minerals:
        check = minerals[:5]
        arr.append("d"*check.count("d")+"i"*check.count("i")+"s"*check.count("s"))
        minerals = minerals[5:]
    
    result = 0
    arr = arr[:sum(picks)]
    arr.sort()
    for check in arr:
        if picks[0]:
            result += len(check)
            picks[0] -= 1
        elif picks[1]:
            result += check.count("d") * 5 + len(check) - check.count("d")
            picks[1] -= 1
        elif picks[2]:
            result += check.count("d") * 25 + check.count("i") * 5 + check.count("s")
            picks[2] -= 1
    
    return result