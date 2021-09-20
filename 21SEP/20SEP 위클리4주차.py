def solution(table, languages, preference):
    table_dict = {}
    for t in table:
        word = t.split(' ')
        table_dict[word[0]] = [0] + word[1:][::-1]

    result = dict()
    for key, value in table_dict.items():
        result[key] = 0
        for point, lang in zip(preference, languages):
            try:
                result[key] += (value.index(lang) * point)
            except ValueError:
                pass
    answer = [key for key, val in result.items() if max(result.values()) == val]

    return sorted(answer)[0]


# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
#          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
#          "GAME C++ C# JAVASCRIPT C JAVA"]
# languages = ["PYTHON", "C++", "SQL"]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))
