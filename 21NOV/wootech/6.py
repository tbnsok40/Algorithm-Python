def solution(time, plans):
    curr = '호치민'
    timeoff = 0
    for p in plans:
        place, dept, arr = p
        dept_time, dept_state = dept[:-2], dept[-2:]
        arr_time, arr_state = arr[:-2], arr[-2:]
        dept_time, arr_time = int(dept_time), int(arr_time)

        if dept_state == "PM":
            if dept_time == 12 or (0 < dept_time <= 6):
                timeoff += (6 - dept_time)
            else:
                pass

        # AM
        else:
            if dept_time > 9:  # 10, 11
                if dept_time == 10:
                    timeoff += 0.5
                else:
                    timeoff += 1.5
            else:
                timeoff += 2.5
            # if dept_time == 12:
            #     timeoff += 18
            #     print(2, timeoff)
            #
            # elif 12 > dept_time >= 6:
            #     timeoff += (12 - dept_time + 6)
            #     print(3, timeoff)
            #
            # else:
            #     timeoff += (abs(6 - dept_time) + 12)
            #     print(4, timeoff)

        if arr_state == "PM":
            if 1 < arr_time <= 6:  # 12 주의
                timeoff += (arr_time - 1)
            elif arr_time == 12:
                pass
            else:
                timeoff += 5

        if timeoff <= time:
            time -= timeoff
            curr = place

    return curr


time = 3.5
plans = [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]
print(solution(time, plans))
