import numpy as np
# 1'den 10'a kadar olan sayılardan bir NumPy dizisi oluştur.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr = np.arange(1, 11)
print(arr)
# 3x3 boyutunda sıfırlardan oluşan bir matris oluştur.
arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(arr)
arr = np.zeros((3, 3))
print(arr)
# 5x5 boyutunda sadece köşelerinde 1 olan ve geri kalanı 0 olan bir matris oluştur
arr = np.zeros((5, 5))
arr[0, 0] = arr[0, -1] = arr[-1, 0] = arr[-1, -1] = 1
# bu kısım köşegen değerleri 1 olan bir matris oluşturur
arr = np.identity(n=5)
print(arr)
# 1 ile 100 arasında 10 tane rastgele sayı içeren bir dizi oluştur.
arr = np.random.randint(1, 101, 10)
arr = np.random.randint(0, 100, 10)
print(arr)
# Belirli bir dizinin elemanlarını ters çevir
arr = arr[::-1]
print(arr)
arr = np.flip(arr)
print(arr)
# 1 boyutlu bir dizinin boyutunu 2 boyutlu (3x3) bir matrise dönüştür.
arr = np.random.randint(0, 100, 9)
print(arr.shape)
arr = arr.reshape((3, 3))
print(arr.shape)
# np.arange kullanarak 0 ile 1 arasında 0.1 artan bir dizi oluştur.
arr = np.arange(0, 1, 0.1)
print(arr)
# 4x4 boyutunda birim matris (identity matrix) oluştur.
arr = np.identity((4))  # köşegende bulunan veriler 1
print(arr)
# Verilen bir dizide kaç tane tek sayı olduğunu bul.
arr = np.random.randint(0, 100, 20)
print(arr)
print(arr[arr % 2 == 1].size)
# Bir dizinin ortalamasını ve standart sapmasını hesapla.
arr = np.random.randint(0, 100, 20)
print(np.average(arr))
print(np.std(arr))
