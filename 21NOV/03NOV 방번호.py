import sys

N = list(sys.stdin.readline().rstrip())
room_dict = dict()
total = 0
for i in N:
    i = int(i)
    room_dict[i] = room_dict.get(i, 0) + 1
room_dict[10] = (room_dict.get(9, 0) + room_dict.get(6, 0)) / 2
if 6 in room_dict.keys():
    room_dict.pop(6)
if 9 in room_dict.keys():
    room_dict.pop(9)
# print(room_dict)
value = max(room_dict.values())
if value == int(value):
    print(value)
else:
    print(int(value) + 1)
"""
하나가 짝수개이면, 절반으로 나눌 수 있긴한데, 반대쪽이 없어야지.
divmod() 를 쓸까. 3이면 1, 1이 나오는데. 5면 2, 1이 나오고. 
아무튼 나머지가 1이 나오면 최소 몫 + 1 세트가 필요하다는 뜻이여. 이경우엔 반대쪽이 없는 경우. 
6: 3 => 1, 1 
9: 5 => 2, 1  => 8 => 4, 0 : 4세트. 
"""


"""
9999
122

"""
