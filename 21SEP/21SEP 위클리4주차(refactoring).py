def solution(table, languages, preference):
    table_dict = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split(' '):
                table_dict[t.split(' ')[0]] = table_dict.get(t.split()[0], 0) + (6 - (t.split(' ')).index(lang)) * pref
    return sorted(key for key, value in table_dict.items() if (max(table_dict.values()) == value))[0]
    # using lambda
    # return sorted(table_dict.items(), key = lambda item: [-item[1], item[0]])[0][0]
