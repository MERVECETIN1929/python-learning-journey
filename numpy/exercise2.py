import numpy as np
# 5x5 boyutunda rastgele tam sayılardan oluşan bir matris oluştur ve her sütunun ortalamasını bul.
arr = np.array(np.random.randint(0, 100, 25)).reshape((5, 5))
arr_average = [np.average(arr[:, i]) for i in range(arr.shape[1])]
arr_average2 = np.mean(arr, axis=0)
print(arr_average)
print(arr_average2)
# 1 ile 50 arasında rastgele 20 sayı üret, çift olanları başka bir dizide sakla.
arr2 = np.random.randint(1, 51, 20)
filter = arr2 % 2 == 0
arr3 = arr2[filter]
print(arr2)
print(arr3)
# 3x3 bir matris oluştur ve transpozesini al.
arr4 = np.random.randint(1, 100, 9).reshape(3, 3)
print(arr4)
arr4 = np.transpose(arr4)
print(arr4)
# İki aynı boyutta matris oluştur, matris çarpımlarını hesapla.
arr5 = np.random.randint(1, 100, 20).reshape(5, 4)
arr6 = np.random.randint(1, 100, 20).reshape(5, 4)
arr7 = arr5*arr6
print(arr5)
print(arr6)
print(arr7)
# 1 boyutlu bir diziyi 3x4 boyutunda bir matrise yeniden şekillendir.
arr8 = np.random.randint(1, 100, 12)
print(arr8.shape)
arr8.shape = (3, 4)
print(arr8.shape)
# Dizi içindeki en büyük değerin konumunu (indeksini) bul.
print(arr8)
index = np.where(arr8 == np.max(arr8))
index2 = np.argmax(arr8)
print("index", index2)
print(index)
# 0 ile 100 arasında 100 elemanlı bir sayı dizisi oluştur ve kaç tanesi 50'den büyük?
arr9 = np.random.randint(0, 101, 100)
print(arr9)
print(arr9[arr9 > 50].size)
# np.where kullanarak negatif sayıları 0 ile değiştir.
arr10 = np.random.randint(-100, 100, 100)
arr10 = np.where(arr10 < 0, 0, arr10)
print(arr10)
# Bir dizideki tekrar eden elemanları kaldır.
arr11 = np.unique(arr10)
print(arr11)
print(arr11.size)
# np.random.seed kullanarak sabit bir rastgelelik oluştur, aynı sonucu tekrar elde et.
np.random.seed(1236)
print(np.random.randint(10, size=5))
np.random.seed(1236)
print(np.random.randint(10, size=5))
