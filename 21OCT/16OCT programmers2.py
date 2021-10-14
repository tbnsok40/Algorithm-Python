def solution(leave, day, holidays):
    if leave == 30:
        return 30
    calender = [i for i in range(1, 31)]

    if day == "SUN":
        weekend = [1, 7, 8, 14, 15, 21, 22, 28, 29]
    elif day == "MON":
        weekend = [2, 8, 9, 15, 16, 22, 23, 29, 30]
    elif day == "TUE":
        weekend = [5, 6, 12, 13, 19, 20, 26, 27]
    elif day == "WED":
        weekend = [6, 7, 13, 14, 18, 19, 27, 28]
    elif day == "THU":
        weekend = [3, 4, 10, 11, 17, 18, 24, 25]
    elif day == "FRI":
        weekend = [2, 3, 9, 10, 16, 17, 23, 24, 30]
    elif day == "SAT":
        weekend = [1, 2, 8, 9, 15, 16, 22, 23, 29, 30]

    for w in weekend:
        if w in calender:
            calender[w - 1] = 'X'
    for l in holidays:
        if l in calender:
            calender[l - 1] = "X"



holidays = [2, 6, 17, 29]
leave = 3
day = "SUN"
print(solution(leave, day, holidays))
