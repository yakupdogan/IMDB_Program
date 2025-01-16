# Film Serisi Yönetim Sistemi

Bu proje, kullanıcıların film verilerini yönetebileceği bir Python uygulamasıdır. Sistemdeki filmler, bir CSV dosyasına kaydedilir ve kullanıcılar filmleri ekleyebilir, silebilir, arama yapabilir ve sıralama gibi işlemler gerçekleştirebilir.

## Özellikler

- **Tüm Filmleri Görüntüle**: Sistemdeki tüm filmleri listeleyebilirsiniz.
- **Film Sayısı Görüntüle**: Arşivdeki toplam film sayısını görüntüleyebilirsiniz.
- **Rank'a Göre Film Seçimi**: Filmleri rank değerine göre sıralayabilir ve bu sıralamada seçim yapabilirsiniz.
- **Film Arama**: Film adı ile arama yaparak ilgili filmi bulabilirsiniz.
- **Film Ekleme**: Yeni bir film adı ve rank değeri ile arşive film ekleyebilirsiniz.
- **Film Silme**: Belirli bir film ismini girerek arşivden film silebilirsiniz.
- **Arşivi Güncelleme ve Kaydetme**: Güncellenen film verilerini yeni bir CSV dosyasına kaydedebilirsiniz.

## Gereksinimler

- Python 3.12
- Pandas Kütüphanesi

## Kurulum

1. Python 3.x sürümünü sisteminize kurun.
2. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine aşağıdaki komutu yazın:
    ```bash
    pip install pandas
    ```

## Kullanım

### Başlangıç

Programı başlattığınızda, kullanıcıya aşağıdaki işlemler seçenekleri sunulacaktır:

- **1**: Tüm filmleri görmenizi sağlar.
- **2**: Arşivdeki film sayısını gösterir.
- **3**: Rank sırasına göre filmleri sıralar.
- **4**: Rank sayısına göre belirli bir film seçmenizi sağlar.
- **5**: Film adı ile arama yapmanızı sağlar.
- **6**: Yeni bir film eklemenizi sağlar.
- **7**: Belirli bir filmi silmenizi sağlar.
- **8**: Verileri günceller ve yeni bir dosyaya kaydeder.
- **q**: Programdan çıkmanızı sağlar.

### Film Ekleme

Filmi eklerken, film adı ve rank değeri girmeniz gerekmektedir. Rank, filmin sıralamasını belirtir.

### Film Silme

Silmek istediğiniz film adını girerek, sistemdeki film arşivinden bu filmi kaldırabilirsiniz.

## Dosya Yapısı

- **film_serisi.csv**: Film verilerini içeren CSV dosyasının yolu.
- **film_serisi.py**: Film serisini yöneten sınıf ve fonksiyonların yer aldığı dosya.
- **film_arsiv.py**: Kullanıcı etkileşimini sağlayan ana program dosyası.

## Katkıda Bulunma

Eğer katkıda bulunmak isterseniz, projeyi forks edebilir ve geliştirmelerinizi pull request olarak gönderebilirsiniz.


