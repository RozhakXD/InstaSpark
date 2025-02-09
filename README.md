# 🚀 InstaSpark - Instagram Bio Generator
![InstaSpark Logo](https://github.com/user-attachments/assets/84899c5c-f461-4402-87f3-f4ca0898619b)

[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/RozhakXD/InstaSpark)
[![Contributors](https://img.shields.io/github/contributors/RozhakXD/instaspark.svg)](https://github.com/RozhakXD/InstaSpark/graphs/contributors)

**InstaSpark** adalah generator bio Instagram bertenaga AI yang membantu Anda membuat bio kreatif, profesional, dan menarik dalam hitungan detik! ✨

## 🌟 Fitur Utama
- **🤖 AI-Powered**: Menggunakan Blackbox AI untuk menghasilkan bio yang unik dan relevan.
- **🎨 Modern UI**: Antarmuka pengguna yang responsif dan elegan dengan Tailwind CSS.
- **🚀 Cepat & Ringan**: Dioptimalkan untuk performa tinggi.
- **📋 Copy-Paste Mudah**: Tombol salin otomatis untuk bio yang dihasilkan.
- **🔒 Validasi Input**: Penanganan error dengan notifikasi yang user-friendly.
- **🌍 Responsif**: Tampilan sempurna di semua perangkat (desktop, tablet, mobile).

## 🛠️ Teknologi yang Digunakan
- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **AI Integration**: Blackbox AI API
- **Tools**: SweetAlert2 untuk notifikasi, FontAwesome untuk ikon

## 📦 Instalasi
1. **Clone Repositori**
    ```bash
    git clone https://github.com/RozhakXD/InstaSpark.git
    cd InstaSpark
    ```
2. **Setup Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. Jalankan Server
   ```bash
   flask run
   ```

## 🎮 Cara Menggunakan
- **Buka Aplikasi**: Akses `http://localhost:5000` di browser.
- **Deskripsikan Diri Anda**: `Saya seorang pendaki gunung yang gemar menjelajahi alam, menaklukkan puncak, dan menikmati keindahan panorama dari ketinggian. Bagi saya, mendaki bukan hanya tentang mencapai puncak, tetapi juga tentang perjalanan, ketahanan, dan kebebasan yang dirasakan di setiap langkah.`
- **Klik "Generate Bio"**: Tunggu AI bekerja! ⚡
- **Salin Bio**: Gunakan tombol salin untuk menyalin bio ke clipboard. 📋

## 📚 API Reference
Generate Bio
```http
POST /api/generate/
```
Request Body:
```json
{
  "description": "Saya seorang desainer grafis yang suka traveling!"
}
```
Response Sukses:
```json
{
  "status": true,
  "message": "🎨 Desainer Grafis | 🌍 Travel Enthusiast | ✨ DM for collab!"
}
```

## 📸 Tangkapan Layar
![Images](https://github.com/user-attachments/assets/a8ab4513-da22-48b2-8f38-701180454f18)

## 📝 Catatan Penting
- **API Key**: Pastikan Anda memiliki API Key dari Blackbox AI untuk menggunakan fitur AI.
- **Environment Variables**: Simpan semua konfigurasi sensitif di file .env.
- **Testing**: Sebelum deploy ke production, pastikan untuk melakukan testing menyeluruh.
- **Issues**: Jika menemukan bug atau memiliki saran, silakan buka issue.

## 💖 Dukungan (Support)
Jika Anda merasa proyek ini bermanfaat, Anda bisa mendukung saya dengan donasi melalui platform berikut:

- Trakteer: [https://trakteer.id/rozhak_official/tip](https://trakteer.id/rozhak_official/tip)
- PayPal: [https://paypal.me/rozhak9](https://paypal.me/rozhak9)
- Saweria: [https://saweria.co/rozhak09](https://saweria.co/rozhak09)

Setiap donasi sangat berarti dan akan digunakan untuk pengembangan proyek ini lebih lanjut. Terima kasih! ❤️

## 📜 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
