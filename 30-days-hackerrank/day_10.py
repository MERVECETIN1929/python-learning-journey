
if __name__ == '__main__':
    n = int(input().strip())
    result = str()
# alinan sayiyi binary yap
    while n != 0 and n != 1:
        result = result+str(n % 2)
        n = n//2
    result += str(n)
    result = reversed(result)
    count = int()
    buffer_count = int()
    for x in result:
        if x == "1":
            buffer_count += 1
        else:
            if buffer_count > count:
                count = buffer_count
            buffer_count = 0
            # dizi sonunda 1 olursa buffer bunu ekler ama karsilastiramaz o
            # yuzden dongu bitiminde tekara rkontrol olmali
    count = max(count, buffer_count)

    print(count)
