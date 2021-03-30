arrays = [35, 31, 32, 39, 37, 36, 33, 34, 38]


def bubble(array):
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


print(bubble(arrays))
