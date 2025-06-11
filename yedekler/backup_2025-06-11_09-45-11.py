import requests
from datetime import datetime
import base64
import os  # GİZLİ TOKEN'I ALMAK İÇİN

# AYARLAR
GITHUB_USERNAME = "idealinsan"
with open("token.txt") as f:
    GITHUB_TOKEN = f.read().strip()# TOKEN ARTIK GİZLİ YERDEN GELİYOR
REPO_NAME = "-Pad-with-pyhton-code-"  # GitHub'da AYNEN bu isimle oluşturduğun repo
LOCAL_FILE = "main.py"  # Yedeklenecek dosya (kendini yedekliyor!)
GITHUB_PATH = f"yedekler/backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.py"

# DOSYAYI OKU
with open(LOCAL_FILE, "rb") as file:
    content = base64.b64encode(file.read()).decode()

# İSTEĞİ HAZIRLA
url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{GITHUB_PATH}"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}
data = {
    "message": "Replit yedekleme",
    "content": content,
    "branch": "main"
}

# İSTEĞİ GÖNDER
response = requests.put(url, headers=headers, json=data)

# SONUCU KONTROL ET
if response.status_code == 201:
    print("✅ Yedekleme başarılı!")
else:
    print("❌ Hata:", response.status_code)
    print(response.json())