from collections import defaultdict

def sum_of_plays(genre, genres_info):
    filtered_genres_info = filter(lambda x: genre == x[0], genres_info)
    total_cnt = sum(map(lambda x: x[1], filtered_genres_info))
    return total_cnt

def solution(genres, plays):
    genres_info = [(genre, play) for genre, play in zip(genres, plays)]
    genres_info = [(genre, play, sum_of_plays(genre, genres_info), i) for i, (genre, play) in enumerate(genres_info)]
    genres_info.sort(key=lambda x: (-x[2], -x[1], x[3]))
    genres_dict = defaultdict(int)
    result = []
    for genre_info in genres_info:
        if genres_dict[genre_info[0]] == 0:
            genres_dict[genre_info[0]] = 1
            result.append(genre_info[3])
        elif genres_dict[genre_info[0]] == 1: 
            genres_dict[genre_info[0]] = 2
            result.append(genre_info[3])
        elif genres_dict[genre_info[0]] == 2:
            continue
    return result