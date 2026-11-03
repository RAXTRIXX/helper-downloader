#!/data/data/com.termux/files/usr/bin/bash
set -e
pkg update -y
pkg install python ffmpeg -y
python -m pip install -U yt-dlp
termux-setup-storage
echo
echo "Instalasi selesai."
echo "Jalankan: python helper_downloader.py"
