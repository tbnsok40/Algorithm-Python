from collections import defaultdict


def solution(genres, plays):
    genres_dict = defaultdict(list)
    plays_enum = []
    # 곡 수 인덱스 추가
    for idx, ele in enumerate(plays):
        plays_enum.append((idx, ele))
    # 각 장르별 총 곡 수
    sums = dict()
    for k, v in zip(genres, plays):
        try:
            sums[k] += v
        except KeyError:
            sums[k] = v

    # 장르 순서대로 배열
    tem = []
    for k, v in sums.items():
        tem.append((k, v))
    tem = sorted(tem, key=lambda x: -x[1])

    # 장르 별 인덱스, 곡 수 정리
    for k, v in zip(genres, plays_enum):
        genres_dict[k].append(v)

    for i in genres_dict:
        genres_dict[i] = sorted(genres_dict[i], key=lambda x: -x[1])

    result = []
    for t in tem:
        for item in genres_dict[t[0]][:2]:
            result.append(item[0])
    return result

print(solution(genres=["classic", "pop", "classic", "classic", "pop"], plays=[500, 600, 150, 800, 2500]))
