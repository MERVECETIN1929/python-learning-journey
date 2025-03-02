class Difference:
    def __init__(self, a):
        self.__elements = a
        # Daha doğru bir başlangıç değeri
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)
# en büyük sayı ile en küçük sayının farkı listedeki en büyük farkı gösterir.


# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
