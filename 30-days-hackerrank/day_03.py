if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0:
        print("Weird")
    else:
        if (N > 2 and N < 5) or (N > 20):
            print("Not Weird")
        else:
            print("Weird")
