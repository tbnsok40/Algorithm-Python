from collections import deque


def change_hash(array):
    array = array.replace('C#', 'c')
    array = array.replace("D#", 'd')
    array = array.replace("F#", 'f')
    array = array.replace("G#", 'g')
    array = array.replace("A#", 'a')
    return array


def solution(m, musicinfos):

    m = change_hash(m)
    answer = ('(None)', None)

    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = change_hash(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] is None) or (time > answer[1]):
                answer = (title, time)
                print(answer)
        return answer[0]

m = "ABC#"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

# C#을 꼭 C#으로 뒀어야 할까? 노노 => 소문자 c로 바꿔버려도 결과를 도출하는데 아무 문제 없다.
# 결과를 도출하는 과정도 중요하지만, 결과를 헤치지 않는 선에서 과정은 내맘대로 만들어도 된다.
# 답이 여러개인 경우, 없는 경우 고려해야 한다.


# 배운것: str 자료형만 replace는 str 용 메소드
# 시간 처리, split()을 저렇게 다룰 수 있구나 배웠다.
# melody_played => 나는 divmod해서 딱 맞아떨어지게 구하려했는데, 굳이 그럴필요없다. 길게 늘어뜨려놓고 슬라이싱 때려도, 시간복잡도 늘어나지 않는다.
# 결과가 여러개일 때, time이 긴 것 대로 처리하는 법 예술.
