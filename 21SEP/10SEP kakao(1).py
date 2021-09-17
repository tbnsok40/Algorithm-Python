from collections import defaultdict


def solution(id_list, report, k):
    id_dict = dict()
    for id in id_list:
        id_dict[id] = [set(), 0]
    count_report = defaultdict(set)
    for string in report:
        user_id, report_id = string.split(' ')
        count_report[user_id].add(report_id)  # 이건 누가 신고했는가에 대한 고민이없다. 그래서 틀렸음.
        id_dict[user_id][0].add(report_id)
    count_report_ = dict()
    for count in count_report:
        count_report_[count] = len(count_report[count])
    number_report = defaultdict(int)
    for value in id_dict.values():
        for v in value[0]:
            number_report[v] += 1
    report_mail = []
    for num in number_report:
        if number_report[num] >= k:
            report_mail.append(num)
    for key, value in id_dict.items():
        for v in value[0]:
            if v in report_mail:
                value[1] += 1
    answer = []
    for id in id_list:
        answer.append(id_dict[id][1])
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]  # ["con", "ryan"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2  # 3
print(solution(id_list, report, k))
