def solution(dartResult):
    mul = {"S":1, "D":2, "T":3}
    dart = []
    stack = {"num":-1, "mul":"", "bonus":""}
    
    i = 0
    while dartResult:
        if dartResult[i].isdigit():
            if stack["num"] >= 0:
                print(stack)
                dart.append(stack)
                stack = {"num":-1, "mul":"", "bonus":""}
            if dartResult[i:i+2] == "10":
                stack["num"]= 10
                dartResult = dartResult[1:]
            else:
                stack["num"] = int(dartResult[i])
        elif dartResult[i].isalpha():
            stack["mul"] = dartResult[i]
        elif dartResult[i] in "*#":
            stack["bonus"] += dartResult[i]
            if dart and dartResult[i] == "*":
                dart[-1]["bonus"] += "*"
        dartResult = dartResult[1:]
    if stack["num"] >= 0:
        dart.append(stack)
        
    result = 0
    for info in dart:
        n = info["num"] ** mul[info["mul"]]
        if "*" in info["bonus"]:
            n *= 2**info["bonus"].count("*")
        if "#" in info["bonus"]:
            n *= -1
        result += n
        
    return result