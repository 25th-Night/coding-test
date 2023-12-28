def solution(wallpaper):
    min_r, min_c, max_r, max_c = 50, 50, 0, 0
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == "#":
                min_r = min(min_r, r)
                min_c = min(min_c, c)
                max_r = max(max_r, r+1)
                max_c = max(max_c, c+1)
    return [min_r, min_c, max_r, max_c]