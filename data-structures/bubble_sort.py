def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)-1):
        swapped = False
        for j in range(len(unsorted_list)-1-i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j +
                                                1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True
        if not swapped:
            return unsorted_list
        print(unsorted_list)
    return unsorted_list


print(bubble_sort([7, 12, 9, 11, 3, 1, 85]))
