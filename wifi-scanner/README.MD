# WiFi Scanner Web App

## 🚨 Legal Warning
**HANYA UNTUK JARINGAN YANG ANDA MILIKI!**  
Penggunaan di jaringan orang lain tanpa izin adalah pelanggaran hukum.

## 🛠️ Setup di Termux (Android)
```bash
# Instalasi Termux
pkg update && pkg upgrade -y
pkg install python nodejs-lts git -y

# Clone proyek
git clone https://github.com/your-username/wifi-scanner.git
cd wifi-scanner

# Setup backend
cd backend
pip install -r requirements.txt
pkg install networkmanager -y
python scanner.py

# Setup frontend
cd ../frontend
npm install
npm start