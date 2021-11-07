def solution(log):
    N = len(log) // 2
    total = 0
    for i in range(N):
        start = i * 2
        end = start + 1

        hour1, min1 = map(int, log[start].split(":"))
        hour2, min2 = map(int, log[end].split(":"))
        # print(hour2, (min2))
        diff_min = (min2) - (min1)
        diff_hour =(hour2) -(hour1)
        if diff_min < 0:
            result_hour = (diff_hour - 1) * 60
            result_min = abs(diff_min)
        else:
            result_hour = diff_hour * 60
            result_min = abs(diff_min)

        result = result_min + result_hour
        if result < 5:
            result = 0
        elif result >= 105:
            result = 105
        total += result

    hour, min = divmod(total, 60)
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(min)) == 1:
        min = '0' + str(min)
    return "{0}:{1}".format(hour, min)


log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
print(solution(log))
"""

["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]

["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]
	
"""