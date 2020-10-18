name, gender_pref, max_dist = input().split()
max_dist = int(max_dist)
# if gender_pref == 'MF' or 'FM':
#     gender_pref = 'MF'

answer = []
for _ in range(int(input())):
    partners_name, gender, dist = input().split()
    dist = int(dist)
    if ((gender_pref == gender) or (gender in gender_pref)) & (max_dist>=dist):
        answer.append(partners_name)

if answer == []:
    print("No one yet")
else:
    answer.sort() #lexicographically 고려해주지 않아서 계속 틀렸움
    for i in range(len(answer)):
        print(answer[i])
