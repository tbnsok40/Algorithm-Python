# for _ in range(int(input())):
#
#     name, date, birth, courses = input().split()
#     date = date.split('/')
#     year = int(date[0])
#
#     birth = birth.split('/')
#     year_birth = int(birth[0])
#     courses = int(courses)
#     if year >=2010:
#         print(name, 'eligible')
#     elif year_birth >= 1991:
#         print(name, 'eligible')
#     elif courses < 41:
#         print(name, 'coach petitions')
#     else:
#         print(name, 'ineligible')