import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yt_dlp

# Video İndirme Fonksiyonu
def download_video():
    url = url_entry.get ().strip ()
    if not url:
        messagebox.showerror ("Hata", "Lütfen bir YouTube URL'si girin!")
        return

    save_path = filedialog.askdirectory () # Kaydedilecek klasörü seçtir
    if not save_path:
        return # Kullanıcı iptal ederse

    # İndirme başlamadan önce progress bar'ı sıfırla
    progress_bar['value'] = 0
    progress_label.config (text="İndirme Durumu: Başlatılıyor...")

    # Ayarlar
    options = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s', # Video başlığına göre kaydet
        'progress_hooks': [progress_hook],
    }

    # Sadece ses seçilmişse
    if audio_only.get ():
        options['format'] = 'bestaudio/best'
        options['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        resolution = resolution_choice.get ()
        options['format'] = f'bestvideo[height<={resolution}] + bestaudio / best'

    # Video İndirme
    try:
        download_button.config (state='disabled')  # İndirme sırasında butonu devre dışı bırak
        with yt_dlp.YoutubeDL (options) as ydl:
            ydl.download ([url])
            messagebox.showinfo ("Başarılı", "Video başarıyla indirildi!")
    except Exception as e:
        messagebox.showerror ("Hata", f"Video indirilemedi: {e}")
    finally:
        download_button.config (state='normal')  # İşlem bitince butonu tekrar aktif et

# İlerleme Çubuğu
def progress_hook(d):
    if d['status'] == 'downloading':
        # Yüzde bilgisini al ve progress bar'ı güncelle
        try:
            # Yüzde string'ini float'a çevir (örn: "45.5%" -> 45.5)
            percent = float (d['_percent_str'].replace ('%', ''))
            progress_bar['value'] = percent

            # İndirme hızı ve kalan süre bilgilerini al
            speed = d.get ('_speed_str', 'N/A')
            eta = d.get ('_eta_str', 'N/A')

            # Detaylı ilerleme bilgisini göster
            progress_label.config (
                text=f"İndiriliyor: %{percent:.1f} | Hız: {speed} | Kalan Süre: {eta}"
            )
        except:
            progress_label.config (text="İndiriliyor...")

    elif d['status'] == 'finished':
        progress_bar['value'] = 100
        progress_label.config (text="İşleniyor... Lütfen bekleyin.")

    elif d['status'] == 'error':
        progress_label.config (text="Hata Oluştu!")
        progress_bar['value'] = 0

    root.update_idletasks ()


# Ana pencere
root = tk.Tk ()
root.title ("YouTube Video Downloader (yt-dlp)")
root.geometry ("600x400")  # Pencereyi biraz daha büyüttük

# Frame oluştur (düzen için)
main_frame = ttk.Frame (root, padding="10")
main_frame.pack (fill=tk.BOTH, expand=True)

# URL Girişi
ttk.Label (main_frame, text="YouTube URL'si:").pack (pady=5)
url_entry = ttk.Entry (main_frame, width=60)  # Entry'yi biraz daha genişlettik
url_entry.pack (pady=5)

# Çözünürlük Seçimi
ttk.Label (main_frame, text="Çözünürlük Seçin:").pack (pady=5)
resolution_choice = ttk.Combobox (main_frame, values=["360", "480", "720", "1080", "2K", "4K"])
resolution_choice.set ("720")
resolution_choice.pack (pady=5)

# Sadece Ses Seçeneği
audio_only = tk.BooleanVar ()
ttk.Checkbutton (main_frame, text="Sadece Ses (MP3) İndir", variable=audio_only).pack (pady=5)

# İndirme Butonu
download_button = ttk.Button (main_frame, text="Videoyu İndir", command=download_video)
download_button.pack (pady=10)

# Progress Frame
progress_frame = ttk.Frame (main_frame)
progress_frame.pack (fill=tk.X, pady=10)

# Progress Bar
progress_bar = ttk.Progressbar (
    progress_frame,
    orient='horizontal',
    mode='determinate',
    length=400
)
progress_bar.pack (fill=tk.X, pady=5)

# Progress Label
progress_label = ttk.Label (progress_frame, text="İndirme Durumu: Bekleniyor")
progress_label.pack (pady=5)

# Ana döngü
root.mainloop ()