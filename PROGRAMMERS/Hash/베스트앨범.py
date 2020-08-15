# def solution(genres, plays):
#
#     # set
#     album = list()
#     index = [i for i in range(len(plays))]
#     for idx in zip(index, genres, plays):
#         album.append(idx)
#
#     # dict
#     album_dic = {}
#     for ge, pl in zip(genres, plays):
#         try:
#             album_dic[ge] += pl
#         except:
#             album_dic[ge] = pl
#     album_dic = sorted(album_dic,reverse=True)
#     print(album_dic)
#     return album
# print(solution(genres,plays))


# 1. 일단 장르별 줄을 세워야 한다.
# 2. 장르내에서 탑2 만 줄을 세워 return
# 2-1. 세가지(idx, genre, play)를 하나의 세트로 묶어 버리자.
# 3. 나머지 장르에 대해서도 반복
genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays=[500, 600, 150, 800, 2500]
from collections import defaultdict
def solution(genres, plays):
    play_count_by_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)
    for song_id, genre, play in zip(counter(),genres,plays):
        play_count_by_genre[genre]+= play
        songs_in_genre[genre].append((-play, song_id))

    print(play_count_by_genre, songs_in_genre)
    # print(sorted(songs_in_genre['classic']))
    # print(songs_in_genre['pop'])
    genre_in_order = sorted(play_count_by_genre.keys(), key=lambda g: play_count_by_genre[g], reverse=True)
    answer = list()
    for genre in genre_in_order:
        answer.extend([song_id for minus_play, song_id in sorted(songs_in_genre[genre])[:2]])
    return answer
def counter():
      i = 0
      while True:
          yield i
          i += 1
print(solution(genres,plays))