from collections import deque


def solution(m, musicinfos):
    N = len(m)
    total_time = []
    for music in musicinfos:
        times = music.split(",")[:2]
        play_time = [int(time[1]) - int(time[0]) for time in zip(times[0].split(":"), times[1].split(":"))]
        time = play_time[0] * 60 + play_time[1]
        music_len = music.split(",")[3]
        div, mod = divmod(time, len(music_len))
        temp = list(div * music_len + music_len[:mod])
        temp_deque = deque()
        for idx, i in enumerate(temp):
            if i == "#":
                s = temp_deque.pop()
                temp_deque.append(s + "#")
                continue
            temp_deque.append(i)

        total_time.append((time, temp_deque, music.split(",")[2]))
    for i in total_time:
        for j in range(len(i[1])):
            if list(i[1])[j:N + j] == list(m):
                return i[2]


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

# C#을 꼭 C#으로 뒀어야 할까? 노노 => 소문자 c로 바꿔버려도 결과를 도출하는데 아무 문제 없다.
# 결과를 도출하는 과정도 중요하지만, 결과를 헤치지 않는 선에서 과정은 내맘대로 만들어도 된다.