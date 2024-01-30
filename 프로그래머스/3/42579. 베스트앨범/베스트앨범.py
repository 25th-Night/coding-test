from collections import defaultdict

def solution(genres, plays):
    play_cnt = defaultdict(int)
    for genre, play in zip(genres, plays):
        play_cnt[genre] += play
    
    info = [ [genre, play_cnt[genre], play, i] for i, (genre, play) in enumerate(zip(genres, plays))]
    info.sort(key=lambda x: (-x[1], -x[2], x[3]))
    play_genre = defaultdict(int)
    result = []
    for i in info:
        if play_genre[i[0]] < 2:
            result.append(i[3])
            play_genre[i[0]] += 1
    return result