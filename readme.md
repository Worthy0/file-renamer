# Dosya Yeniden Adlandırıcı ve Yedekleme Aracı

Bu Python betiği, belirtilen bir klasördeki dosyaları yeniden adlandırır:

- Boşlukları ve özel karakterleri, kullanıcı tarafından belirtilen karakterlerle değiştirir.
- Dosya adlarını küçük harfe dönüştürür (isteğe bağlı).
- Yedekleme klasörü oluşturarak orijinal klasörün yedeğini alır.
- Yeniden adlandırılan ve atlanan dosyaları raporlar.

## Özellikler

- **Özel Karakter Değiştirme:** Boşlukları `_` veya `-` ile değiştirme seçeneği.
- **Küçük Harfe Dönüştürme:** Dosya adlarını küçük harfe dönüştürme (isteğe bağlı).
- **Yedekleme:** Orijinal klasörün yedeği otomatik olarak oluşturulur.
- **Hata Yönetimi:** Geçersiz yollar, boş klasörler ve izin hatalarını düzgün şekilde ele alır.

## Kullanım Talimatları

1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/Worthy0/file-renamer.git
   ```
