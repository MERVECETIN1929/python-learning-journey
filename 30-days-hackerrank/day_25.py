# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def check_prime(number):
    # sayı 2 ise asal sayıdır
    if number == 2:
        return print("Prime")
    # sayı 1 ise asal değildir
    if number == 1:
        return print("Not prime")
    # başlangıç değeri 2 olmalı. bitiş değeri ise sayının karekökü +1. çünkü sayının kareköküne kadar zaten bir böleni varsa sayıyı asallıktan çıkartır ve devamını kontrol etmeye gerek olmaz
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return print("Not prime")

    print("Prime")


number_count = int(input())
for i in range(number_count):
    number = int(input())
    check_prime(number)
