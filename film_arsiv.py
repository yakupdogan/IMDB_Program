
from film_serisi import *
import time
import os

print("""
Film arşivine hoşgeldiniz.

İŞLEMLER;

1.Tüm Filmler
2.Arşivdeki film sayısı
3.Kategorileri gör
4.Rank sayısına göre film seçiniz
5.Film arama
6.Film Ekleme
7.Film Silme
8.Arşivi güncelle ve kaydet

Çıkmak için 'q' ya basınız.

""")
film = Film_serisi("./film_serisi.csv")
while True:
    islemler = input("İşlem seçiniz : ")
    if(islemler) == "q":
        print("Sistemden çıkış yapılıyor.")
        break
    elif(islemler == "1"):
        print("Tüm filmler yükleniyor....")
        time.sleep(1)
        print(film.Film_gor())
    elif(islemler == "2"):
        time.sleep(1)
        print(film.Film_adet())
    elif(islemler == "3"):
        time.sleep(1)
        print(film.rank_getir())
    elif(islemler == "4"):
        satir = input("Hangi satırdaki filmi çekmek istiyorsunuz : ")
        print(film.rank_sec(satir))

    elif(islemler == "5"):
        isim = input("Lütfen aramak istediğiniz filmi giriniz : ")
        print("Film aranıyor....")
        time.sleep(1)
        print(film.film_ara(isim))
    elif(islemler == "6"):
        film_adi = input("LÜtfen ekemek istediğiniz filmin adını giriniz: ")
        satir = input("LÜtfen hangi satıra yerleştirmek istediğinizi girin: ")
        print(film.film_ekle(film_adi, satir))
    elif(islemler == "7"):
        film_adi = input("Lütfen silmek istediğiniz filmi giriniz : ")
        time.sleep(1)
        print(film.film_sil(film_adi))

    elif(islemler == "8"):
        masaustu_yolu = os.path.join(os.path.expanduser("~"), "Desktop", "yenifilm_serisi.csv")

        film.data.to_csv(masaustu_yolu, index=False)
        print(f"Veriler başarıyla {masaustu_yolu} yoluna kaydedilmiştir..")

    else:
        print("Geçersiz işlem girdiniz...")
