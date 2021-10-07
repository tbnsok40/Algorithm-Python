from itertools import product, chain


def solution(word):
    basic = ["A", "E", 'I', "O", "U"]
    word_set = basic[:]

    """ permutation 과 product 의 차이
    for i in range(2, 6):
        for j in permutations(basic, i):  # permutation 과 product의 차이구나. => permutation: 순열, 각 원소를 한번씩 조합 <=> product 는 각 원소를 여러번 조합
            word_set.append(''.join(j))
    word_set.sort()
    for i in range(2, 6):
        word_set += list(map(list, product(basic, repeat=i)))
    result = sorted(list(map(lambda x: ''.join(x), word_set)))
    # 사실상, A, E, I, O, U 를 조합하여, 쫙 펼치고 소팅하면 된다.
    
    itertools.chain() : iterable 객체를 인수로 받아 하나의 iterator 로 반환
    """
    for i in range(2, 6):
        word_set = chain(word_set, list(map(list, product(basic, repeat=i))))
        # word_set += list(map(list, product(basic, repeat=i)))
    result = sorted(list(map(lambda x: ''.join(x), word_set)))
    return result.index(word) + 1

