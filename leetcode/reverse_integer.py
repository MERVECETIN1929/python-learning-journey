def reverse(x):
    number = int()
    if x < 0:
        number = str(x)
        number = number[1:]
        number = number[::-1]
        number = "-"+number

    else:
        number = str(x)
        number = number[::-1]
    number = int(number)

    if number > 2**31 or number < -1*(2**31)-1:
        return 0
    else:
        return number


rakam = int(input("rakamını gir: \n"))
print(reverse(rakam))
