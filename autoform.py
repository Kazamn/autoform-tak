import os
import json
import time
import subprocess
from dotenv import load_dotenv
from google import genai
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

REFERENSI_DROPDOWN = """
DAFTAR MENU FORM TAK:

1. Jika Kategori = "Pengembangan Karakter"
   - Jenis Kegiatan: ['Self-Management', 'Relationship Management', 'Leadership', 'Entrepreneur Mindset', 'Literasi Baca dan Tulis', 'Resiliensi, Kesehatan Fisik dan Mental']
   - Tingkat Kegiatan: ['Universitas']
   - Keikutsertaan: ['Peserta']

2. Jika Kategori = "Kompetisi"
   - Jenis Kegiatan: ['Kompetisi BELMAWA', 'Kompetisi Mandiri']
   - Tingkat Kegiatan: ['Regional', 'Universitas', 'Internasional', 'Nasional']
   - Keikutsertaan: ['Juara 1', 'Juara 2', 'Juara 3', 'Juara Harapan', 'The Most inspiring atau Penghargaan Setara lainnya', 'Finalis', 'Peserta']

3. Jika Kategori = "Organisasi"
   - Jenis Kegiatan: ['Organisasi Kemahasiswaan']
   - Tingkat Kegiatan: ['Nasional', 'Regional', 'Universitas', 'Internasional']
   - Keikutsertaan: ['Pengurus - Ketua atau Wakil Ketua', 'Pengurus - Sekretaris, Bendahara, Pengurus Inti atau setara', 'Pengurus - Koordinator Bidang/Divisi atau setara', 'Pengurus - Staf Bidang', 'Anggota Aktif']

4. Jika Kategori = "Seminar"
   - Jenis Kegiatan: ['Seminar']
   - Tingkat Kegiatan: ['Regional', 'Universitas', 'Internasional', 'Nasional']
   - Keikutsertaan: ['Pembicara', 'Moderator/MC', 'Peserta']

5. Jika Kategori = "Kepanitiaan"
   - Jenis Kegiatan: ['Kepanitiaan Kegiatan']
   - Tingkat Kegiatan: ['Kegiatan ≥ 10 bulan', 'Kegiatan 7 s.d. 9 bulan', 'Kegiatan 4 s.d. 6 bulan', 'Kegiatan 1 s.d. 3 bulan']
   - Keikutsertaan: ['Ketua atau Wakil Ketua', 'Sekretaris, Bendahara, Pengurus Inti atau setara', 'Koordinator Bidang/Divisi', 'Anggota/ Peserta/Liaison Officer (LO)']

6. Jika Kategori = "Pengembangan Karier"
   - Jenis Kegiatan: ['Career Preparation Training III (Bimbingan Karier Kelas Besar/Kelompok Koseling Karier)', 'Career Preparation Training I (Soft-Skill)', 'Career Preparation Training II (Industrial Seminar)']
   - Tingkat Kegiatan: ['Universitas']
   - Keikutsertaan: ['Peserta']

7. Jika Kategori = "Wawasan Kebangsaan"
   - Jenis Kegiatan: ['Anti Korupsi', 'Anti Napza', 'Anti Radikalisme', 'Pencegahan Kekerasan Seksual dan Perundungan', 'Green Campus', 'Literasi Keuangan', 'Perlindungan Data Pribadi dan Literasi Digital']
   - Tingkat Kegiatan: ['Universitas']
   - Keikutsertaan: ['Peserta']

8. Jika Kategori = "PKKMB"
   - Jenis Kegiatan: ['PKKMB']
   - Tingkat Kegiatan: ['Universitas']
   - Keikutsertaan: ['Peserta']

9. Jika Kategori = "Penelitian (Skema PPM atau Mandiri)"
   - Jenis Kegiatan: ['Tim Penelitian']
   - Tingkat Kegiatan: ['Dana Eksternal', 'Dana Internal']
   - Keikutsertaan: ['Anggota Tim Penelitian']

10. Jika Kategori = "Publikasi Ilmiah (Skema PPM atau Mandiri)"
   - Jenis Kegiatan: ['Jurnal dan Prosiding Internasional', 'Jurnal dan Prosiding Nasional', 'Presenter International Conference', 'Presenter Konferensi Nasional']
   - Tingkat Kegiatan: ['Prosiding', 'Internasional Q1', 'Internasional Q2', 'Internasional Q3', 'Internasional Q4']
   - Keikutsertaan: ['Penulis Pertama', 'Anggota Penulis']

11. Jika Kategori = "Pengabdian Masyarakat (Skema PPM atau Mandiri)"
   - Jenis Kegiatan: ['Tim Pengabdian Masyarakat']
   - Tingkat Kegiatan: ['Nasional', 'Universitas', 'Wilayah', 'Internasional']
   - Keikutsertaan: ['Ketua/Wakil Ketua', 'Sekretaris/Bendahara/Koordinator Bidang', 'Anggota/Peserta/Volunteer']

12. Jika Kategori = "Pembelajaran di Luar Kampus"
   - Jenis Kegiatan: ['Pertukaran Mahasiswa', 'Magang/Praktik Kerja', 'Bekerja', 'Asistensi Mengajar di Satuan Pendidikan', 'Proyek Kemanusiaan', 'Studi/Proyek Independen', 'Membangun Desa/Kuliah Kerja Nyata Tematik', 'Bela Negara', 'Pembinaan Kompetisi', 'Pembelajaran di Luar Kampus']
   - Tingkat Kegiatan: ['Pembelajaran di Luar Kampus']
   - Keikutsertaan: ['Pembelajaran di Luar Kampus']

13. Jika Kategori = "Kekayaan Intelektual"
   - Jenis Kegiatan: ['Hak Kekayaan Intelektual']
   - Tingkat Kegiatan: ['Internasional', 'Nasional']
   - Keikutsertaan: ['Paten', 'Desain Industri, Hak atas Topografi Sirkuit Terpadu', 'Hak Cipta, Merek/Logo, Karya ber-ISBN']

14. Jika Kategori = "Duta Kampus"
   - Jenis Kegiatan: ['Duta Kampus (Senior Resident, Buddy, Marketing Crew, Tutor, Peer, Counselor, Asisten Dosen/Laboratorium, Fasilitator, Mentor, Petugas Upacara, Tnjidor, DLL)']
   - Tingkat Kegiatan: ['10 s.d. 12 bulan', '7 s.d. 9 bulan', '4 s.d 6 bulan', '1 s.d. 3 bulan']
   - Keikutsertaan: ['Baik', 'Sangat Baik', 'Cukup']

15. Jika Kategori = "Rekognisi"
   - Jenis Kegiatan: ['Rekognisi']
   - Tingkat Kegiatan: ['Universitas', 'Internasional', 'Nasional', 'Regional']
   - Keikutsertaan: ['Penerima']

16. Jika Kategori = "Entrepreneurship"
   - Jenis Kegiatan: ['Entrepreneurship dengan Dokumen Legalitas Usaha', 'Entrepreneurship Tidak Memiliki Dokumen Legalitas Usaha']
   - Tingkat Kegiatan: ['Lebih dari 2 tahun', 'antara 1 - 2 tahun', 'Kurang dari 1 tahun']
   - Keikutsertaan: ['omset > 500jt', '250 - 500 jt', '150 - 250 jt', '101 - 200jt', '51 - 100 jt', '< 50 juta']

17. Jika Kategori = "Program Bahasa dan Budaya"
   - Jenis Kegiatan: ['Program Bahasa dan Budaya Mahasiswa Asing']
   - Tingkat Kegiatan: ['Universitas']
   - Keikutsertaan: ['Peserta']

18. Jika Kategori = "Kegiatan Program Studi Pendidikan Jarak Jauh"
   - Jenis Kegiatan: ['Kegiatan Mahasiswa Program Studi Pendidikan Jarak Jauh']
   - Tingkat Kegiatan: ['Universitas']
   - Keikutsertaan: ['Peserta']

19. Jika Kategori = "Latihan Keterampilan Manajemen Mahasiswa (LKMM)"
   - Jenis Kegiatan: ['Peserta Latihan Keterampilan Manajemen Mahasiswa (LKMM)']
   - Tingkat Kegiatan: ['Tingkat Dasar', 'Tingkat Menengah', 'Tingkat Lanjut']
   - Keikutsertaan: ['Peserta Lulus']

20. Jika Kategori = "Pelatihan"
   - Jenis Kegiatan: ['Pelatihan']
   - Tingkat Kegiatan: ['Internasional', 'Nasional', 'Universitas']
   - Keikutsertaan: ['Peserta']

21. Jika Kategori = "Sertifikasi"
   - Jenis Kegiatan: ['Sertifikasi']
   - Tingkat Kegiatan: ['Internasional', 'Nasional']
   - Keikutsertaan: ['Peserta']

22. Jika Kategori = "Pameran Karya"
   - Jenis Kegiatan: ['Pameran Karya']
   - Tingkat Kegiatan: ['Internasional', 'Nasional', 'Regional', 'Universitas']
   - Keikutsertaan: ['Peserta']
"""

def ekstrak_sertifikat_ke_json(pdf_path):
    print(f"Membaca file: {pdf_path} ...")
    sertifikat_file = client.files.upload(file=pdf_path)
    
    prompt = f"""
    Kamu adalah sistem ekstraksi data otomatis untuk pengisian form Transkrip Aktivitas Kemahasiswaan (TAK) Telkom University.
    
    Berikut adalah referensi pilihan dropdown yang tersedia di sistem:
    {REFERENSI_DROPDOWN}
    
    Patuhi struktur key JSON berikut dan pastikan kategori menggunakan teks persis dari referensi:
    - "tanggal_selesai": (Cari kata kunci tanggal penyelesaian atau terbit sertifikat. Wajib ubah ke format DD/MM/YYYY)
    - "tanggal_mulai": (Cari tanggal pendaftaran/enrollment atau tanggal mulai kursus. Jika tidak tertulis eksplisit, silakan HITUNG MUNDUR dari "tanggal_selesai" dengan asumsi kecepatan belajar sangat intensif, yaitu 12 jam per hari. Contoh: jika durasi total 90 jam, hitung mundur sekitar 7-8 hari dari tanggal selesai. Jika benar-benar tidak ada referensi durasi/waktu mulai, samakan dengan "tanggal_selesai". Wajib ubah ke format DD/MM/YYYY)
    - "deskripsi": (Buat 1-2 kalimat ringkas materi yang dipelajari dan sebutkan penyelenggaranya. ATURAN DURASI: Jika ada informasi durasi >= 5 jam, WAJIB gunakan kata estimasi di akhir kalimat. Contoh: "dengan estimasi waktu pembelajaran sekitar X jam" atau "dengan perkiraan penyelesaian X jam". JANGAN tulis "dengan total durasi X jam" secara absolut. Abaikan penulisan durasi jika < 5 jam.)
    - "penyelenggara": (Nama institusi penerbit)
    - "nama_kegiatan": (Judul kelas atau kegiatan)
    - "nama_kegiatan_inggris": (Terjemahkan ke bahasa Inggris)
    - "jenis_kategori": (PILIH SATU kategori yang paling tepat dari referensi. ATURAN PENTING: Jika sertifikat berupa kelulusan kelas/kursus/training seperti dari Dicoding atau Coursera, WAJIB pilih "Pelatihan". Pilih "Sertifikasi" HANYA jika itu adalah kelulusan ujian sertifikasi profesi resmi.)
    - "jenis_kegiatan": (PILIH SATU teks persis dari Jenis Kegiatan pada kategori terpilih)
    - "tingkat_kegiatan": (PILIH SATU teks persis dari Tingkat Kegiatan pada kategori terpilih)
    - "keikutsertaan": (PILIH SATU teks persis dari Keikutsertaan pada kategori terpilih)
    - "jenis_penyelenggara": (Analisis institusi penerbit. Jika diselenggarakan oleh Telkom University atau organisasi internal di dalamnya, tulis "Internal". Jika dari luar kampus seperti Coursera, Dicoding, dll, tulis "External")
    
    Keluarkan HANYA output JSON murni tanpa markdown.
    """

    daftar_model = [
        "gemini-3.7-flash",    
        "gemini-3.6-flash",   
        "gemini-3.5-flash"    
    ]
    
    hasil_teks = ""
    
    for nama_model in daftar_model:
        try:
            print(f"  -> Menganalisis dokumen menggunakan {nama_model} ...")
            response = client.models.generate_content(
                model=nama_model, 
                contents=[sertifikat_file, prompt]
            )
            hasil_teks = response.text.strip()
            print(f"  [V] Berhasil mengekstrak data dengan {nama_model}!")
            break  
            
        except Exception as e:
            print(f"  [!] {nama_model} gagal digunakan. Beralih ke model cadangan...")
            time.sleep(2) 
            
    client.files.delete(name=sertifikat_file.name)
    
    if not hasil_teks:
        print("\n[ERROR] Semua model AI gagal memproses dokumen. Server mungkin sedang sibuk atau kuota API habis.")
        return None
        
    if hasil_teks.startswith("```json"):
        hasil_teks = hasil_teks[7:-3].strip()
    elif hasil_teks.startswith("```"):
        hasil_teks = hasil_teks[3:-3].strip()
        
    return json.loads(hasil_teks)

def klik_dropdown(wait, driver, nama_formcontrol, teks_target):
    if not teks_target or teks_target == "-":
        return
        
    try:
        print(f"-> Memilih '{teks_target}' pada kotak {nama_formcontrol}...")
        xpath_dropdown = f"//ng-select[@formcontrolname='{nama_formcontrol}']"
        dropdown = wait.until(EC.presence_of_element_located((By.XPATH, xpath_dropdown)))

        area_klik = dropdown.find_element(By.CSS_SELECTOR, '.single')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", area_klik)
        time.sleep(0.1)
        driver.execute_script("arguments[0].click();", area_klik)
        time.sleep(0.1)

        xpath_pilihan = f"{xpath_dropdown}//select-dropdown//li[contains(., '{teks_target}')]"
        pilihan = driver.find_element(By.XPATH, xpath_pilihan)
        driver.execute_script("arguments[0].click();", pilihan)
        time.sleep(0.1) 
    except Exception as e:
        print(f"  [X] Gagal memilih '{teks_target}'.")
        try:
            driver.execute_script("arguments[0].click();", area_klik)
        except:
            pass

def isi_form_tak(driver, data_json, path_ke_pdf):
    try:
        print("\n" + "="*50)
        print("BERHASIL TERHUBUNG KE BROWSER!")
        print("Pastikan kamu SUDAH login.")
        input("JIKA SUDAH SIAP, TEKAN ENTER DI TERMINAL INI UNTUK MEMULAI INJEKSI... ")
        print("="*50 + "\n")
        
        # 1. Pastikan berada di tab yang benar
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if "telkomuniversity.ac.id" in driver.current_url or "tak" in driver.current_url:
                break
                
        # 2. Refresh halaman ke form input baru 
        print("Mereset halaman form TAK...")
        driver.get("https://situ-kem.telkomuniversity.ac.id/tak/input-tak")
        time.sleep(1) 
        
        wait = WebDriverWait(driver, 5)
        print("Mulai menginjeksi data ke form TAK secara otomatis...\n")
        
        # 3. Tahun Akademik 
        dropdown_tahun = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='year']")))
        dropdown_tahun.click()
        time.sleep(0.1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='2025/2026']"))).click()
        time.sleep(0.1)
        
        # 4. Tanggal Mulai dan Selesai
        input_tgl_mulai = wait.until(EC.presence_of_element_located((By.ID, "start_date")))
        input_tgl_mulai.clear()
        input_tgl_mulai.send_keys(data_json.get("tanggal_mulai", ""))
        
        input_tgl_selesai = wait.until(EC.presence_of_element_located((By.ID, "end_date")))
        input_tgl_selesai.clear()
        input_tgl_selesai.send_keys(data_json.get("tanggal_selesai", ""))
        time.sleep(0.1)

        # 5. EKSEKUSI DROPDOWN KATEGORI & KEGIATAN
        klik_dropdown(wait, driver, "category", data_json.get("jenis_kategori"))
        klik_dropdown(wait, driver, "activity", data_json.get("jenis_kegiatan"))
        klik_dropdown(wait, driver, "level", data_json.get("tingkat_kegiatan"))
        klik_dropdown(wait, driver, "participation", data_json.get("keikutsertaan"))

        # 6. Deskripsi
        xpath_deskripsi = "//textarea[@formcontrolname='description']"
        input_deskripsi = wait.until(EC.presence_of_element_located((By.XPATH, xpath_deskripsi)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_deskripsi)
        time.sleep(0.1)
        input_deskripsi.clear()
        input_deskripsi.send_keys(data_json.get("deskripsi", ""))
        
        # 7. Upload Berkas Sertifikat
        input_file = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        path_sertifikat = os.path.abspath(path_ke_pdf) 
        input_file.send_keys(path_sertifikat)

        # 8. DROPDOWN JENIS PENYELENGGARA (INTERNAL/EXTERNAL)
        klik_dropdown(wait, driver, "organizer_type_id", data_json.get("jenis_penyelenggara"))

        # 9. Penyelenggara
        input_organizer = wait.until(EC.presence_of_element_located((By.NAME, "organizer")))
        input_organizer.clear()
        input_organizer.send_keys(data_json.get("penyelenggara", ""))
        
        # 10. Nama Kegiatan
        input_act_name = wait.until(EC.presence_of_element_located((By.NAME, "activity_name_id")))
        input_act_name.clear()
        input_act_name.send_keys(data_json.get("nama_kegiatan", ""))
        
        # 11. Nama Kegiatan Inggris
        input_act_en = wait.until(EC.presence_of_element_located((By.NAME, "activity_name_en")))
        input_act_en.clear()
        input_act_en.send_keys(data_json.get("nama_kegiatan_inggris", ""))
        
        print("\nSemua data dan file berhasil diinjeksikan secara otomatis!")
        print("Selesai! Silakan review formulir di browser dan centang pernyataan persetujuan sebelum Submit.")
        
    except Exception as e:
        print(f"Terjadi error pada Selenium: {e}")
    finally:
        print("Selesai mengisi satu form.")

def pilih_file_pdf():
    folder_pdf = "sertifikat_pdf"
    
    if not os.path.exists(folder_pdf):
        os.makedirs(folder_pdf)
        print(f"\n[INFO] Folder '{folder_pdf}' baru saja dibuat!")
        print(f"Silakan pindahkan semua file PDF kamu ke dalam folder '{folder_pdf}' tersebut lalu jalankan ulang script.")
        return None
        
    daftar_pdf = [file for file in os.listdir(folder_pdf) if file.lower().endswith('.pdf')]
    
    if not daftar_pdf:
        print(f"\nTidak ada file PDF yang ditemukan di dalam folder '{folder_pdf}'.")
        return None
        
    print(f"\n=== DAFTAR FILE SERTIFIKAT (Di dalam folder '{folder_pdf}') ===")
    for index, file in enumerate(daftar_pdf):
        path_lengkap = os.path.join(folder_pdf, file)
        
        ukuran_bytes = os.path.getsize(path_lengkap)
        ukuran_mb = ukuran_bytes / (1024 * 1024)
        peringatan = " ⚠️ (MELEBIHI 2 MB!)" if ukuran_mb > 2 else f" ({ukuran_mb:.2f} MB)"
        print(f"[{index + 1}] {file}{peringatan}")
        
    while True:
        try:
            pilihan = int(input("\nMasukkan nomor file yang ingin diproses (contoh: 1): "))
            if 1 <= pilihan <= len(daftar_pdf):
                file_terpilih = daftar_pdf[pilihan - 1]
                path_lengkap = os.path.join(folder_pdf, file_terpilih)
                
                ukuran_bytes = os.path.getsize(path_lengkap)
                if ukuran_bytes > 2 * 1024 * 1024:
                    print(f"\n[X] DITOLAK: Ukuran file '{file_terpilih}' mencapai {ukuran_bytes / (1024*1024):.2f} MB.")
                    print("Web TAK Telkom membatasi maksimal 2 MB. Silakan kompres PDF kamu lalu coba lagi.")
                    continue 
                    
                print(f"File terpilih: {file_terpilih}\n")
                
                return path_lengkap 
            else:
                print("Nomor di luar jangkauan. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

def buka_browser_otomatis(pilihan):
    url_tak = "https://situ-kem.telkomuniversity.ac.id/tak/input-tak"
    
    if pilihan == '1':
        path_browser = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        data_dir = r"C:\edge_debug"
    elif pilihan == '2':
        path_browser = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        data_dir = r"C:\chrome_debug"
    elif pilihan == '3':
        path_browser = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        data_dir = r"C:\brave_debug"
    else:
        return False

    if not os.path.exists(path_browser):
        print(f"\n[X] Gagal: Tidak dapat menemukan browser di '{path_browser}'")
        print("Pastikan browser tersebut sudah terinstall di komputermu.")
        return False

    print("\nMembuka browser dalam mode debugging...")
    subprocess.Popen([path_browser, "--remote-debugging-port=9222", f"--user-data-dir={data_dir}", url_tak])
    time.sleep(1) 
    return True

def inisialisasi_browser():
    print("\n" + "="*50)
    print("=== PILIH BROWSER UNTUK OTOMATISASI ===")
    print("[1] Microsoft Edge")
    print("[2] Google Chrome")
    print("[3] Brave Browser")
    print("="*50)
    
    while True:
        pilihan = input("Masukkan nomor browser (contoh: 1): ").strip()
        
        if pilihan in ['1', '2', '3']:
            if not buka_browser_otomatis(pilihan):
                continue 
            
            try:
                if pilihan == '1':
                    print("Menyambungkan ke Microsoft Edge...")
                    options = EdgeOptions()
                    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    service = EdgeService(EdgeChromiumDriverManager().install())
                    return webdriver.Edge(service=service, options=options)
                    
                elif pilihan == '2':
                    print("Menyambungkan ke Google Chrome...")
                    options = ChromeOptions()
                    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    service = ChromeService(ChromeDriverManager().install())
                    return webdriver.Chrome(service=service, options=options)
                    
                elif pilihan == '3':
                    print("Menyambungkan ke Brave Browser...")
                    options = ChromeOptions()
                    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    service = ChromeService(ChromeDriverManager().install())
                    return webdriver.Chrome(service=service, options=options)
                    
            except Exception as e:
                print(f"\n[GAGAL] Tidak bisa terhubung ke browser.")
                print(f"Error detail: {e}")
                exit()
        else:
            print("[X] Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")

if __name__ == "__main__":
    driver_utama = inisialisasi_browser()

    while True:
        print("\n" + "="*50)
        file_pdf = pilih_file_pdf()
        
        if file_pdf:
            data_sertifikat = ekstrak_sertifikat_ke_json(file_pdf)
            if data_sertifikat:
                isi_form_tak(driver_utama, data_sertifikat, file_pdf)
        else:
            print("Proses dilewati karena tidak ada file PDF yang dipilih.")
            
        print("\n" + "="*50)
        ulangi = input("Apakah kamu ingin memproses sertifikat lain? (y/n): ").strip().lower()
        
        if ulangi != 'y':
            print("Terima kasih! Menutup program otomatisasi...")
            break