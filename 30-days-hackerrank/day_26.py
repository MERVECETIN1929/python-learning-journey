# day month year
returned = list(map(int, input().split()))
due = list(map(int, input().split()))
if returned[2] < due[2]:
    print(0)
elif returned[2] > due[2]:
    print(10000)
else:
    if returned[1] <= due[1]:
        if returned[0] <= due[0]:
            print(0)
        else:
            print(15*(returned[0]-due[0]))
    else:
        print(500*(returned[1]-due[1]))
