Autoform TAK Telkom University

Script otomatisasi untuk mengekstrak informasi dari sertifikat PDF menggunakan **Google Gemini AI** dan menginputkannya secara otomatis ke form web Transkrip Aktivitas Kemahasiswaan (TAK) Telkom University.

Persyaratan Sistem
* Sistem operasi Windows dan Mac.
* Browser Chromium (Edge / Chrome / Brave / Opera).
* API Key aktif dari Google Gemini (melalui Google AI Studio).

Cara Instalasi & Penggunaan

1. Download script

2. Konfigurasi API Key
Buat sebuah file baru bernama .env di dalam folder proyek, lalu isi dengan format berikut:

GEMINI_API_KEY=masukkan_api_key_gemini

3. Siapkan Dokumen Sertifikat
Jalankan script untuk pertama kali agar folder sertifikat_pdf dibuat secara otomatis. Pindahkan semua file sertifikat (maksimal 2MB per file) ke dalam folder tersebut.

4. Jalankan Aplikasi
Buka aplikasi dengan mengeklik dua kali pada file autoform.bat atau jalankan langsung dari terminal:

python autoform.py


⚠️ Catatan Penting
Pastikan Anda sudah Login ke portal TAK Telkom University di browser yang terbuka secara otomatis sebelum menekan tombol ENTER di terminal untuk memulai proses injeksi.
