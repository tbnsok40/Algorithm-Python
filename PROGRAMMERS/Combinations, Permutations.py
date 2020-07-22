import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

# ''.join => 각각의  리스트 원소를 문자열로 합친다.
# map()의 첫번째 인자는 type만 올줄 알았는데, join 메서드도 가능.
travel_buddy = ['lim','kim','han']
print(list(map('+'.join, itertools.permutations(travel_buddy,2))))