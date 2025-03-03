# kelimenin harf sayısı kadar deneme hakkı olacak
# her harf bildiğinde keimedeki yerleri açılacak kalan yerler ise - ile dolu olacak
# kullanıcının bilemediği harleri bir set dizininde saklayacağım.
# peki bitme kontrolü nasıl sağlanacak?
import random

words = ['ASLAN', 'İSTANBUL', 'DOKTOR', 'ELMA', 'TITANIC', 'TOKYO', 'MÜHENDIS', 'KARPUZ', 'MATRIX',
         'TIMSAH', 'KANADA', 'AVUKAT', 'ÇILEK', 'GLADYATÖR', 'MOSKOVA', 'AŞÇI', 'BROKOLI', 'YUNUS', 'BREZILYA']


def indeksleri_bul(girilen_harf):
    return [i for i in range(
            len(secilen_kelime)) if girilen_harf == secilen_kelime[i]]


def kelime_güncelle(kelime, girilen_harf, indeksler):
    kelime = list(kelime)
    for i in indeksler:
        kelime[i] = girilen_harf
    return "".join(kelime)


def kullanici_bilgilendirme(sayac, tahmin_kelimesi, kelimede_yok):
    print(
        f"kalan tahmin sayınız: {sayac}. Şimdiye kadarki kullandığınız kelimeler: {" ".join(kelimede_yok)}")
    print(f"Oluşturduğunuz kelime: {tahmin_kelimesi}")


kelimede_yok = set()
secilen_kelime = random.choice(words)
tahmin_kelimesi = str("-"*len(secilen_kelime))
sayac = len(secilen_kelime)
print(secilen_kelime)
while sayac > 0:
    girilen_harf = input(
        f"Bir harf giriniz: \n").upper()
    if girilen_harf in secilen_kelime:
        indeksler = indeksleri_bul(girilen_harf)
        tahmin_kelimesi = kelime_güncelle(
            tahmin_kelimesi, girilen_harf, indeksler)
    else:
        if girilen_harf in kelimede_yok:
            kullanici_bilgilendirme(sayac, tahmin_kelimesi, kelimede_yok)
        else:
            kelimede_yok.add(girilen_harf)
            sayac -= 1
    kullanici_bilgilendirme(sayac, tahmin_kelimesi, kelimede_yok)
    if tahmin_kelimesi == secilen_kelime:
        print("Tebrikler...")
        break
