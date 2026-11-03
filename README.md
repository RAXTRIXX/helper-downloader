# HELPER DOWNLOADER
Downloader video berbasis yt-dlp untuk Termux.

## Install
```bash
pkg update && pkg install git python ffmpeg -y
python -m pip install -U yt-dlp
termux-setup-storage
```
Izinkan akses penyimpanan Android saat diminta.

## Jalankan
```bash
python helper_downloader.py
```

Hasil disimpan ke:
`~/storage/shared/Movies/HelperDownloader`

## Catatan
- Dukungan platform dan kualitas berubah mengikuti yt-dlp.
- Tidak semua video dapat diunduh; video privat, login-required, atau dibatasi mungkin gagal.
- Gunakan hanya untuk konten milik sendiri atau yang diizinkan. Hormati hak cipta dan ketentuan platform.
