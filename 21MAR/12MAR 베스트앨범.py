from collections import defaultdict
def solution(genres, plays):
    count_genre = dict() # defaultdict(int)로 선언하면 아래와 같은 짓 안해도 된다.
    for a, b in zip(genres, plays):
        try:
            count_genre[a] += b
        except:
            count_genre[a] = b
    sorted_genre = sorted(count_genre, key=lambda item: item[1], reverse=True) # count_genre, count_genre.items()
    print(sorted_genre)
    # (id, play_hits) 형싱으로 저장
    new_plays = list()
    for idx, play in enumerate(plays):
        new_plays.append((idx, play))

    # 장르 별, (id, play_hits) 저장
    song_dict = defaultdict(list)
    for a, b in zip(genres, new_plays):
        song_dict[a].append(b)

    for i in song_dict:
        sum = 0
        for j in song_dict[i]:
            sum += j[1]

    for i in song_dict:
        # sorted_song = list(map(sorted(), lambda x: x[1], reverse=True)) # 망한 코드
        song_dict[i] = sorted(song_dict[i], key=lambda x: x[1], reverse=True) # 제대로 된 코드
        # print("temp: ", song_dict[i])

    result = []
    for genre in sorted_genre:
        # print(song_dict[genre][:2])
        for li in song_dict[genre][:2]: #indexError 예외처리 해보기, 무작정 :2로 해버려서 인덱스 터진
            result.append(li[0])
    return result


from collections import defaultdict
# def solution(genres, plays):
#     answer = []
#     genres_plays = defaultdict(int)
#     genres_songs = defaultdict(lambda: [])
#     i = 0
#     for g, p in zip(genres, plays):
#         genres_plays[g] += p
#         genres_songs[g].append((i, p))
#         i += 1
#
#     sorted_genres = sorted(genres_plays.items(), key=(lambda x: x[1]), reverse=True)
#
#     for g in sorted_genres:
#         print(g)
#         sorted_g = sorted(genres_songs[g[0]], key = lambda x: x[1], reverse=True)
#         answer.append(sorted_g[0][0])
#         if len(sorted_g) > 1:
#             answer.append(sorted_g[1][0])
#     print(answer)
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# plays = [500, 2500, 500, 800, 2500]
print(solution(genres, plays))