def solution(table, languages, preference):
    table_dict = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split(' '):
                table_dict[t.split(' ')[0]] = table_dict.get(t.split()[0], 0) + (6 - (t.split(' ')).index(lang)) * pref
    return sorted(key for key, value in table_dict.items() if (max(table_dict.values()) == value))[0]

    # using lambda
    # return sorted(table_dict.items(), key = lambda item: [-item[1], item[0]])[0][0]


# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
#          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
#          "GAME C++ C# JAVASCRIPT C JAVA"]
# languages = ["PYTHON", "C++", "SQL"]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))
