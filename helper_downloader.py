#!/usr/bin/env python3
import os, sys, subprocess, shutil, time
from pathlib import Path

RESET="\033[0m"; GREEN="\033[92m"; CYAN="\033[96m"; MAGENTA="\033[95m"; RED="\033[91m"; WHITE="\033[97m"; BOLD="\033[1m"

BASE=Path.home()
OUT=BASE/"storage"/"shared"/"Movies"/"HelperDownloader"
if not (BASE/"storage"/"shared").exists():
    OUT=BASE/"Movies"/"HelperDownloader"

def clear(): os.system("clear")
def loading(msg):
    frames="⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(20):
        print(f"\r{CYAN}{frames[i%len(frames)]} {msg}...{RESET}",end="",flush=True)
        time.sleep(.06)
    print("\r"+" "*50+"\r",end="")
def banner():
    print(f"""{MAGENTA}{BOLD}
╦ ╦╔═╗╦  ╔╦╗╔═╗╦═╗  ╔╦╗╔═╗╦ ╦╔╗╔
║ ║║╣ ║   ║ ║╣ ╠╦╝   ║║║╣ ║ ║║║║
╚═╝╚═╝╩═╝ ╩ ╚═╝╩╚═  ═╩╝╚═╝╚═╝╝╚╝
{CYAN}       HELPER VIDEO DOWNLOADER{RESET}
{WHITE}     TikTok • YouTube • Pinterest{RESET}
""")
def pause(): input(f"\n{WHITE}Tekan ENTER untuk kembali...{RESET}")
def install_deps():
    if not shutil.which("yt-dlp"):
        print("yt-dlp belum terpasang.")
        ans=input("Pasang sekarang? (y/n): ").lower()
        if ans=="y":
            subprocess.run([sys.executable,"-m","pip","install","-U","yt-dlp"])
    if not shutil.which("ffmpeg"):
        print("Catatan: ffmpeg disarankan untuk menggabungkan video/audio.")
        subprocess.run(["pkg","install","ffmpeg","-y"],check=False)
def download():
    clear(); banner()
    url=input(f"{CYAN}Tempel link video: {WHITE}").strip()
    if not url.startswith(("https://","http://")):
        print(f"{RED}Link tidak valid.{RESET}"); pause(); return
    if not shutil.which("yt-dlp"):
        print(f"{RED}yt-dlp belum terpasang. Jalankan: pip install -U yt-dlp{RESET}")
        pause(); return
    OUT.mkdir(parents=True,exist_ok=True)
    print(f"\n{GREEN}Folder tujuan: {OUT}{RESET}")
    print("Pilih kualitas:")
    print("1. Terbaik yang tersedia")
    print("2. Maksimal 720p")
    print("3. Maksimal 480p")
    q=input("Pilihan [1]: ").strip() or "1"
    fmt={
        "1":"bestvideo*+bestaudio/best",
        "2":"bestvideo[height<=720]+bestaudio/best[height<=720]",
        "3":"bestvideo[height<=480]+bestaudio/best[height<=480]"
    }.get(q,"bestvideo*+bestaudio/best")
    print(f"\n{MAGENTA}Memulai download...{RESET}")
    cmd=[
        "yt-dlp",
        "--no-playlist",
        "--windows-filenames",
        "-f",fmt,
        "--merge-output-format","mp4",
        "-o",str(OUT/"%(title).120s.%(ext)s"),
        url
    ]
    try:
        result=subprocess.run(cmd)
        if result.returncode==0:
            print(f"\n{GREEN}{BOLD}✓ Download selesai!{RESET}")
            print(f"Video tersimpan di:\n{OUT}")
            print("Buka Galeri → Album/Video atau Movies → HelperDownloader.")
            print("Jika tidak muncul, tunggu beberapa saat atau buka ulang Galeri.")
        else:
            print(f"\n{RED}Download gagal. Link mungkin privat, tidak didukung, atau dibatasi.{RESET}")
            print("Coba perbarui yt-dlp: pip install -U yt-dlp")
    except KeyboardInterrupt:
        print("\nDownload dibatalkan.")
    pause()
def main():
    while True:
        clear(); banner()
        print(f"""{WHITE}{BOLD}╭────────────── MENU ──────────────╮{RESET}
 {GREEN}1{RESET}  📥 Download video dari link
 {GREEN}2{RESET}  📂 Buka folder download
 {GREEN}3{RESET}  🔄 Update yt-dlp
 {GREEN}4{RESET}  ℹ️  Panduan
 {RED}0{RESET}  Keluar
{WHITE}{BOLD}╰────────────────────────────────╯{RESET}
""")
        c=input(f"{CYAN}HELPER-DL{GREEN} ➜ {RESET}").strip()
        if c=="1": download()
        elif c=="2":
            OUT.mkdir(parents=True,exist_ok=True)
            subprocess.run(["termux-open",str(OUT)],check=False); pause()
        elif c=="3":
            subprocess.run([sys.executable,"-m","pip","install","-U","yt-dlp"])
            pause()
        elif c=="4":
            clear(); banner()
            print("• Tempel URL video yang bisa diakses publik.")
            print("• Unduhan hanya untuk konten yang kamu miliki/diizinkan.")
            print("• Beberapa platform atau video dapat membatasi unduhan.")
            print("• Login/cookies tidak diminta oleh tool ini.")
            print("• Hasil tersimpan di Movies/HelperDownloader.")
            pause()
        elif c=="0": print("Terima kasih!"); break
        else: print("Pilihan tidak valid."); time.sleep(1)
if __name__=="__main__":
    main()
