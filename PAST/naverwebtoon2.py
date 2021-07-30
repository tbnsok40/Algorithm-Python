from collections import deque

s = list("2(12333)")


def count_letters(s):
    return ''.join(s[2:-1] * int(s[0]))


# print(count_letters(s))


def check_bracket_one_set(s):
    if s.count(")") == 1 and s.count("(") == 1:
        # return s[2:-1] * int(s[0])
        return True

    else: False

    # if "(" in s or ")" in s:
    #     return False
    # else:
    #     return True


def solution(compressed):
    result = ''
    left = []
    stack = []
    number_stack = []
    deq_compressed = deque(compressed)
    temp_compressed = list(compressed)
    print(temp_compressed)

    temp = []
    for idx, s in enumerate(compressed):
        # 문자, 숫자(2자리), 괄호 끼리 묶어서 넣어야한다.
        # if s == ")" or s == "(":
        #     temp.append(s)
        try:
            if int(s):
                print(s)
                if int(compressed[idx - 1]):
                    _s = temp.pop()
                    print('hi', _s)
                #
                    temp.append(_s + s)

        # s = deq_compressed.popleft()

        # if s == "(":
        #     starting_idx = idx - 1
        #     stack.append(starting_idx)
        # elif s == ")":
        #     number = stack.pop()
        #     print(temp_compressed[number: idx + 1])
        #     print(''.join(int(compressed[number]) * compressed[starting_idx + 2: idx]))
        #     temp_compressed[number: idx + 1] = list(''.join(int(compressed[number]) * compressed[starting_idx + 2: idx]))
        #     # return ''.join(int(compressed[number]) * compressed[starting_idx + 2: idx])
        #     temp_compressed





# compressed = "3(hi)"
compressed = "2(32(hi)co)"

print(solution(compressed))
