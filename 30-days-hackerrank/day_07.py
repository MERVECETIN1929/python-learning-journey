n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
arr2 = str()
for i in range(len(arr)-1, -1, -1):
    arr2 = arr2+str(arr[i])+" "
print(arr2)
