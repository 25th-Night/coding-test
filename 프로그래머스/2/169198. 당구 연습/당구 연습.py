def solution(m, n, startX, startY, balls):
    answer = []
    for bx, by in balls:
        diffX = startX-bx
        diffY = startY-by
        
        left = (startX+bx)**2 + (diffY**2)
        right = ((m-startX)+(m-bx))**2 + (diffY**2)
        top = (diffX**2) + ((n-startY)+(n-by))**2
        bottom = (diffX**2) + (startY+by)**2
        
        if not diffX:
            if diffY > 0:
                res = min(left, right, top)        
            else:
                res = min(left, right, bottom)   
        elif not diffY:
            if diffX > 0:
                res = min(right, top, bottom)        
            else:
                res = min(left, top, bottom)         
        else:
            res = min(left, right, top, bottom)
            
        answer.append(res)
    return answer