# YouTube Video Downloader

Bu proje, YouTube videolarını indirmek için kullanılan basit ve kullanıcı dostu bir masaüstü uygulamasıdır. yt-dlp kütüphanesini kullanarak videoları farklı çözünürlüklerde indirebilir veya sadece ses dosyası olarak MP3 formatında kaydedebilirsiniz.

## Özellikler

- Farklı video çözünürlüklerinde indirme seçeneği (360p, 480p, 720p, 1080p, 2K, 4K)
- Sadece ses (MP3) indirme seçeneği
- İndirme ilerleme çubuğu
- İndirme hızı ve kalan süre göstergesi
- Kullanıcı dostu arayüz

## Gereksinimler

- Python 3.6 veya üzeri
- FFmpeg (ses dönüşümü için gerekli)

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/ahazer/youtube-downloader.git
cd youtube-downloader
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. FFmpeg'i yükleyin:
- Windows için: [FFmpeg İndirme Sayfası](https://ffmpeg.org/download.html)
- Linux için: `sudo apt-get install ffmpeg`
- macOS için: `brew install ffmpeg`

## Kullanım

1. Uygulamayı başlatın:
```bash
python youtube_download.py
```

2. YouTube video URL'sini girin
3. İstediğiniz çözünürlüğü seçin veya "Sadece Ses" seçeneğini işaretleyin
4. "Videoyu İndir" butonuna tıklayın
5. Kaydetmek istediğiniz klasörü seçin

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 