"""
selection sort -> picking minimum and switch
"""
arrays = [35, 31, 32, 39, 37, 36, 33, 34, 38]


def selection(array):
    for i in range(len(array)):
        mini = array[i]
        idx = i
        for j in range(i + 1, len(array)):
            if mini > array[j]:
                mini = array[j]
                idx = j
        array[idx] = array[i]
        array[i] = mini

    return array


print(selection(arrays))
