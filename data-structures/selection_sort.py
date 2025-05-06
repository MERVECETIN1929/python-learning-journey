def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i  # en küçük değerin indexi
        for j in range(i + 1, len(arr)):  # kalan kısmı tara
            if arr[j] < arr[min_index]:
                min_index = j  # yeni minimum bulundu
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap işlemi
    return arr


print(selection_sort([7, 12, 9, 11, 3]))
