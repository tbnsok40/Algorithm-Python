str1 = "FRANCE"
str2 = 'french'

str1 = "E=M*C^2"
str2 = "e=m*c^2"

str1 = "AA_bb_aa_AA"
str2 = "BBB"

str1 = "ABDDD"
str2 = "DDEFGHH"

str1 = "AACCC"
str2 = "A A A A A C C C C"
import math
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    temp1, temp2 = [], []

    # 문자 1차 가공
    temp1 = [(str1[i] + str1[i + 1]) for i in range(len(str1) - 1) if (str1[i] + str1[i + 1]).isalpha()]
    temp2 = [(str2[i] + str2[i + 1]) for i in range(len(str2) - 1) if (str2[i] + str2[i + 1]).isalpha()]

    uni_temp = []
    for i in temp1:
        for j in temp2:
            if i == j:
                uni_temp.append(i)
                temp2.remove(j)
                break
    all_temp = temp1 + temp2

    if len(uni_temp) != 0 and len(all_temp) != 0:
        return math.floor((len(uni_temp) / len(all_temp)) * 65536)
    else:
        return 65536
# test 5, 13 error
print(solution(str1, str2))

