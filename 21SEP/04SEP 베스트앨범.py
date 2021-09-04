from collections import defaultdict


def solution(genres, plays):
    genres_dict = defaultdict(list)
    plays_enum = []
    for idx, ele in enumerate(plays):
        plays_enum.append((idx, ele))

    for k, v in zip(genres, plays_enum):
        genres_dict[k].append(v)

    for i in genres_dict:
        genres_dict[i] = sorted(genres_dict[i], key=lambda x: -x[1])

    temp = []
    for i in genres_dict:
        temp.append((i, genres_dict[i][0][1]))

    temp = sorted(temp, key=lambda x: -x[1])
    result = []
    for t in temp:
        k = (genres_dict[t[0]])[:2]
        for kk in k:
            result.append(kk[0])

    return result


print(solution(genres=["classic", "pop", "classic", "classic", "pop"], plays=[500, 600, 150, 800, 2500]))
