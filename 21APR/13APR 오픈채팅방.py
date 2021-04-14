def solution(record):
    answer, tmp = list(), list()
    id_name = {"Enter": "님이 들어왔습니다.",
               "Leave": "님이 나갔습니다."}
    temp = [(idx, *string.split(' ')) for idx, string in enumerate(record)]
    for i in temp:
        if i[1] != 'Leave':
            id_name[i[2]] = i[3]
        if i[1] == "Enter" or i[1] == "Leave":
            tmp.append('{},{}'.format(i[2], i[1]))
    for i in tmp:
        a, b = i.split(',')
        answer.append('{}{}'.format(id_name[a], id_name[b]))

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

result = ["Prodo님이 들어왔습니다.",
          "Ryan님이 들어왔습니다.",
          "Prodo님이 나갔습니다.",
          "Prodo님이 들어왔습니다."]

"""
(순서, 아이디, 이름, 메시지)
(1, uid1234, Muzi, 님이 들어왔습니다.)
(2, uid4567, Prodo, 님이 들어왔습니다.)
(3, uid4567, -, 님이 나갔습니다.)
(4, uid4567, Prodo, 님이 들어왔습니다.)
(5, uid4567, Ryan, -)

최종 상태의 이름을 저장 => set[1]의 아이디값에 따라 이름 변경
=> 딕셔너리에, 아이디를 키로 하여 이름을 value로 하여 저장

이름이 바뀔 때의 메시지는 출력하지 않는다.


"""
print(solution(record))




# python tricks
# how to pick only and all even numbers
# a = [1,2,3,4,5,6,7,8,9]
# print(a[1::2])