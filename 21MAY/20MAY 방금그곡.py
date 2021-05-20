def solution(m, musicinfos):
    N = len(m)
    total_time = []
    for music in musicinfos:
        times = music.split(",")[:2]
        play_time = [int(time[1]) - int(time[0]) for time in zip(times[0].split(":"), times[1].split(":"))]
        total_time.append(play_time[0] * 60 + play_time[1])



    print(total_time)
    answer = ''
    return answer


# dictionay,or set


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
