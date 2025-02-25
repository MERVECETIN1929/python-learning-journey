# upper case
from functools import reduce
fruits = ['apple', 'banana', 'cherry']
fruits = list(map(lambda x: x.upper(), fruits))
print(fruits)
# her stringin ilk karakterini döndür
words = ['apple', 'banana', 'cherry']
chars = list(map(lambda x: x[0], words))
print(chars)
# stringden boşlukları kaldırma
s = ['  hello  ', '  world ', ' python  ']
s = list(map(str.strip, s))
print(s)
# dereceden Fahrenheit'ı hesapla 1.8+32
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda x: x*1.8+32, celsius))
print(fahrenheit)
# en uzun kelimeyi bul
words = ["apple", "banana", "cherry", "blueberry", "strawberry"]
longest_word = str(reduce(lambda x, y: x if len(x) > len(y) else y, words))
print(longest_word)
# pozitif -negatif ayrıştır
numbers = [-5, 3, -1, 7, -9, 2, 0, -4]
positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))
print(positive_numbers)
print(negative_numbers)
# çift ise sayı karesini tek ise kendisini döndür
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = list(map(lambda x: x**2 if x % 2 == 0 else x, numbers))
print(numbers)
# pozitif sayıların karesini al
numbers = [-5, 3, -2, 7, 0, 4, -9]
numbers = list(map(lambda x: x**2, filter(lambda x: x > 0, numbers)))
print(numbers)
# 1den 100e kadar olan 3 ve 5 e bölünen sayıların toplamı
numbers = list(range(1, 101))
sum_numbers = int(
    reduce(lambda x, z: x+z, filter(lambda x: x % 5 == 0 and x % 3 == 0, numbers)))
print(sum_numbers)
