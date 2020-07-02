# def mergeSort(original_list):
#     if len(original_list) < 2:
#         return original_list
#     mid = (len(original_list) // 2)
#     list1 = original_list[:mid]
#     list2 = original_list[mid:]
#     return merge(mergeSort(list1), mergeSort(list2))
#
# def merge(list1, list2):
#     i = 0
#     j = 0
#     merged_list = []
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] > list2[j]:
#             merged_list.append(list2[j])
#             j += 1
#         else:
#             merged_list.append(list1[i])
#             i += 1
#
#     if j == len(list2):
#         merged_list += list1[i:]
#     elif i == len(list1):
#         merged_list += list2[j:]
#
#     return merged_list
#
# x, y = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = a+b
#
# for elements in (mergeSort(c)):
#     print(elements, end =' ')

x,y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(a+b)
print(' '.join(map(str, c)))
