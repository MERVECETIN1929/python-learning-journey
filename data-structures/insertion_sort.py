def insertion_sort(array):
    for i in range(1, len(array)):
        current_index = i
        for j in range(i - 1, -1, -1):
            if array[current_index] < array[j]:
                array[j], array[current_index] = array[current_index], array[j]
                current_index = j
            else:
                break
    return array


print(insertion_sort([7, 12, 9, 11, 3]))
