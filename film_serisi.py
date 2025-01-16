
import pandas as pd
import time
class Film_serisi:
    def __init__(self,dosya_yolu):
        self.dosya_yolu=dosya_yolu
        self.data = pd.read_csv(self.dosya_yolu)

    def Dosyayolu_kaydet(self,yeni_dosya):
        self.dosya_yolu=yeni_dosya
        self.data.to_csv(self.dosya_yolu)

    def Film_gor(self):
        return self.data[["rank","title"]]

    def Film_adet(self):
        return "{} adet film bulunmaktadır..".format(len(self.data))

    def rank_getir(self):
        sirali_data = self.data.sort_values(by = "rank",ascending = True).reset_index(drop=True)

        return sirali_data[["rank","title"]]

    def rank_sec(self,deger):
        try:
            deger = int(deger)
            if(deger > len(self.data)):
                print("Arşivimizde bu kadar film bulunmamaktadır...")
            else:
                print(self.data.iloc[deger - 1])
        except ValueError:
            print("Geçerli bir sayısal değer giriniz...")

    def film_ara(self, film_adi):
        film_adi = film_adi.lower().replace(" ", "")

        sorgu = self.data[self.data["title"].str.replace(" ", "").str.contains(film_adi, case=False, na=False)]

        if not sorgu.empty:
            time.sleep(1)
            filtreli_sorgu = sorgu[["rank", "title"]]
            return filtreli_sorgu
        else:
            return "Aradığınız film bulunamadı...."

    def film_ekle(self,film_adi,rank):
        yeni_film = {"title" : film_adi , "rank" : rank}
        self.data = self.data._append(yeni_film,ignore_index = True)                         #ignore_index in görevi veri eklendikten sonra yeni eklenen satır için sıfırdan index numarası verilir.

        return f"{film_adi} filmi başarıyla eklendi"

    def film_sil(self,film_adi):
        sorgu = self.data[self.data["title"].str.contains(film_adi, case = False, na = False)]


        if not sorgu.empty:
            film_satir = sorgu.index
            self.data =self.data.drop(film_satir)
            self.data.to_csv(self.dosya_yolu)

            return f"{film_adi} başarıyla silindi..."
        else:
            return f"Aradığınız film bulunamamıştır..."





































