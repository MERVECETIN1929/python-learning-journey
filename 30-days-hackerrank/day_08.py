count = int(input())
data = dict()


for _ in range(count):
    datastr = input().split()
    if len(datastr) == 2:
        data[datastr[0]] = datastr[1]


while True:
    try:
        datastr = input().strip()
        if datastr == "":
            break
        print(f"{datastr}={data[datastr]}") if datastr in data else print(
            "Not found")
    except EOFError:
        break
