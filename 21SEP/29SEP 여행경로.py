from collections import defaultdict


# test case 1, 2 failed
def solution(tickets):
    stack = ["ICN"]
    visited = []
    ticket_dict = defaultdict(list)
    for a, b in tickets:
        ticket_dict[a].append(b)
    for key, value in ticket_dict.items():
        ticket_dict.get(key).sort(reverse=True)  # reverse 하지 않아도 된다.
        # ticket_dict.get(key).sort()
    print(ticket_dict)

    while stack:
        # head = stack.pop()
        # visited += [head]
        # if ticket_dict[head]:
        #     ticket = ticket_dict[head].pop()
        #     print(head, ticket)
        #     stack.append(ticket)

        while ticket_dict[stack[-1]]:
            ticket = ticket_dict[stack[-1]].pop()
            stack.append(ticket)
            print(stack)

        visited += [stack.pop()]
    print(ticket_dict)

    return visited


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


# T 1 :
# tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# ans : ["ICN", "B", "ICN", "A", "D", "A"]
#
# T 2: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
# ans : ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
#
# T 3 :
tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
# ans : ["ICN", "COO", "ICN", "BOO", "DOO"]
#
# 4번 반례 해결하니 2번 테케 통과했습니다.
# T 4: \
# tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
# ans : ["ICN", "SFO", "ICN", "SFO", "QRE"]

print(solution(tickets))
