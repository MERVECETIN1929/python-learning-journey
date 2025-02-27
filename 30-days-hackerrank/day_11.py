if __name__ == '__main__':

    arr = []
    current_hourglass = int()
    max_hourglass = int()
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            current_hourglass = sum(arr[i][j:j+3]) + \
                arr[i+1][int((2*j+2)/2)]+sum(arr[i+2][j:j+3])
            if max_hourglass < current_hourglass:
                max_hourglass = current_hourglass
    print(max_hourglass)

"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""
