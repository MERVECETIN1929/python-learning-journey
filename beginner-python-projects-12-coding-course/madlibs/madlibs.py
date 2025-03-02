# elimizde bulunan senaryolara kullanıcıdan aldığımız değerleri birleştirip bir hikaye ortaya çıkaracağız
import random


def check(user_input):
    if len(user_input) == 0:
        return check(input("lütfen giriş yapmayı unutmayın!"))
    else:
        return user_input


senaryolar = [
    "Bugün sabah {isim} ile birlikte {yer}'e gittim. Orada {nesne} bulduk ve çok şaşırdık. Bir anda {hayvan} önümüze atladı ve {fiil} yapmaya başladı! O sırada {ünlü} gelip bizi kurtardı. Bugün gerçekten {sifat} bir gündü.",

    "{isim}, bir gün {yer} adlı gizemli bir yere gitti. Orada {nesne} buldu ve aniden {hayvan} ortaya çıktı! Korkudan {fiil} yaptı. Tam o sırada {ünlü}, ona yardım etti. Bu gerçekten {sifat} bir gündü.",

    "Bir sabah {isim}, {yer}’e gitmeye karar verdi. Yanına {nesne} aldı ve yola çıktı. Ama yolda {hayvan} ile karşılaştı ve korkudan {fiil} yaptı! Neyse ki {ünlü} ona yardım etti. Ne kadar {sifat} bir gündü!"
]

while True:
    senaryo = random.choice(senaryolar)
    isimler = check(
        input("lütfen aralarında boşluk bırakarak isimler girin: ").split())
    yer_isimleri = check(input(
        "lütfen aralarında boşluk bırakarak yer isimleri girin: ").split())
    nesne_isimleri = check(input(
        "lütfen aralarında boşluk bırakarak nesne isimleri  girin: ").split())
    hayvanlar = check(input(
        "lütfen aralarında boşluk bırakarak hayvan isimleri girin: ").split())
    fiiller = check(
        input("lütfen aralarında boşluk bırakarak fiiler girin: ").split())
    ünlüler = check(input(
        "lütfen aralarında boşluk bırakarak ünlü isimleri girin: ").split())
    sifatlar = check(
        input("lütfen aralarında boşluk bırakarak sıfatlar girin: ").split())

    print(senaryo.format(isim=random.choice(isimler), yer=random.choice(yer_isimleri), nesne=random.choice(nesne_isimleri),
                         hayvan=random.choice(hayvanlar), fiil=random.choice(fiiller), ünlü=random.choice(ünlüler), sifat=random.choice(sifatlar)))

    user_continue = input(
        "Oyuna devam etmek ister misiniz? (E: evet, H: hayır)").strip().lower()
    if user_continue in ["e", "h"]:
        if user_continue == "h":
            print("Oyun bitti! Çıkış yapılıyor...")
            break
