import os
import json
import time
import subprocess
import sys
import threading   
import itertools
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

if not api_key:
    print("\n" + "-"*50)
    print("[ERROR] GEMINI API KEY NOT FOUND!")
    print("-"*50)
    print("The application requires an AI access key to read PDFs.")
    print("How to resolve this:")
    print("1. Create a file named exactly '.env' in the same folder as this application.")
    print("2. Open the file.")
    print("3. Insert the following text: GEMINI_API_KEY=insert_your_api_key_here")
    print("\n*You can get a free API Key at: https://aistudio.google.com/app/apikey")
    print("-"*50)
    input("\nPress Enter to exit the application...")
    exit()

client = genai.Client(api_key=api_key)

class Spinner:
    def __init__(self, message="Loading..."):
        self.spinner = itertools.cycle(['-', '\\', '|', '/'])
        self.stop_running = False
        self.message = message
        self.thread = threading.Thread(target=self.spin)

    def spin(self):
        while not self.stop_running:
            sys.stdout.write(f"\r{self.message} {next(self.spinner)}")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * (len(self.message) + 2) + '\r')

    def start(self):
        self.stop_running = False
        self.thread.start()

    def stop(self):
        self.stop_running = True
        self.thread.join()

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

def extract_certificate_to_json(pdf_path):
    print(f"Reading file: {pdf_path} ...")
    certificate_file = client.files.upload(file=pdf_path)
    
    prompt = f"""
    You are an automated data extraction system for filling out the Telkom University Transkrip Aktivitas Kemahasiswaan (TAK) form.
    
    Here is the reference for the available dropdown options in the system:
    {REFERENSI_DROPDOWN}
    
    Comply with the following JSON key structure and ensure the categories use the exact text from the reference:
    - "tanggal_selesai": (Find the completion date or certificate issuance date. MUST be converted to DD/MM/YYYY format)
    - "tanggal_mulai": (Find the enrollment date or course start date. If not explicitly stated, please COUNT BACKWARDS from "tanggal_selesai" assuming a highly intensive learning pace of 12 hours per day. Example: if the total duration is 90 hours, count back around 7-8 days from the completion date. If there is absolutely no reference to duration/start time, make it the same as "tanggal_selesai". MUST be converted to DD/MM/YYYY format)
    - "deskripsi": (Create 1-2 concise sentences in Indonesian of the material learned and mention the organizer. DURATION RULE: If there is duration info >= 5 hours, MUST use the word 'estimasi' at the end of the sentence. Example: "dengan estimasi waktu pembelajaran sekitar X jam" or "dengan perkiraan penyelesaian X jam". DO NOT write "dengan total durasi X jam" absolutely. Ignore duration writing if < 5 hours.)
    - "penyelenggara": (Name of the issuing institution)
    - "nama_kegiatan": (Title of the class or activity)
    - "nama_kegiatan_inggris": (Translate the activity title to English)
    - "jenis_kategori": (CHOOSE ONE most appropriate category from the reference. IMPORTANT RULE: If the certificate is for passing a class/course/training such as from Dicoding or Coursera, MUST choose "Pelatihan". Choose "Sertifikasi" ONLY if it is passing an official professional certification exam.)
    - "jenis_kegiatan": (CHOOSE ONE exact text from Jenis Kegiatan in the selected category)
    - "tingkat_kegiatan": (CHOOSE ONE exact text from Tingkat Kegiatan in the selected category)
    - "keikutsertaan": (CHOOSE ONE exact text from Keikutsertaan in the selected category)
    - "jenis_penyelenggara": (Analyze the issuing institution. If organized by Telkom University or internal organizations within it, write "Internal". If from outside the campus like Coursera, Dicoding, etc., write "External")
    
    Output ONLY pure JSON without markdown.
    """

    model_list = [
        "gemini-3.7-flash",    
        "gemini-3.6-flash",   
        "gemini-3.5-flash"    
    ]
    
    text_result = ""
    
    for model_name in model_list:
        try:
            pesan_loading = f"  -> Analyzing document using {model_name}"
            loading_anim = Spinner(pesan_loading)
            loading_anim.start()
            
            response = client.models.generate_content(
                model=model_name, 
                contents=[certificate_file, prompt]
            )
            
            loading_anim.stop()
            text_result = response.text.strip()
            print(f"  [V] Successfully extracted data with {model_name}!")
            break  
            
        except Exception as e:
            loading_anim.stop() 
            print(f"  [!] {model_name} failed. Switching to backup model...")
            time.sleep(2) 
            
    client.files.delete(name=certificate_file.name)
    
    if not text_result:
        print("\n[ERROR] All AI models failed to process the document. The server might be busy or API quota exceeded.")
        return None
        
    if text_result.startswith("```json"):
        text_result = text_result[7:-3].strip()
    elif text_result.startswith("```"):
        text_result = text_result[3:-3].strip()
        
    return json.loads(text_result)

def click_dropdown(wait, driver, formcontrol_name, target_text):
    if not target_text or target_text == "-":
        return
        
    try:
        print(f"-> Selecting '{target_text}' in the {formcontrol_name} box...")
        dropdown_xpath = f"//ng-select[@formcontrolname='{formcontrol_name}']"
        dropdown = wait.until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))

        click_area = dropdown.find_element(By.CSS_SELECTOR, '.single')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_area)
        time.sleep(0.1)
        driver.execute_script("arguments[0].click();", click_area)
        time.sleep(0.1)

        option_xpath = f"{dropdown_xpath}//select-dropdown//li[contains(., '{target_text}')]"
        option = driver.find_element(By.XPATH, option_xpath)
        driver.execute_script("arguments[0].click();", option)
        time.sleep(0.1) 
    except Exception as e:
        print(f"  [X] Failed to select '{target_text}'.")
        try:
            driver.execute_script("arguments[0].click();", click_area)
        except:
            pass

def fill_tak_form(driver, json_data, pdf_path):
    try:
        print("\n" + "-"*50)
        print("SUCCESSFULLY CONNECTED TO BROWSER!")
        print("Please ensure you are ALREADY logged in.")
        input("Press Enter to Start... ")
        print("-"*50 + "\n")
        
        # 1. Ensure you are on the correct tab
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if "telkomuniversity.ac.id" in driver.current_url or "tak" in driver.current_url:
                break
                
        # 2. Refresh page to new input form
        print("Resetting TAK form page...")
        driver.get("https://situ-kem.telkomuniversity.ac.id/tak/input-tak")
        time.sleep(1) 
        
        wait = WebDriverWait(driver, 5)
        print("Starting automated data injection into TAK form...\n")
        
        # 3. Academic Year
        print("-> Setting academic year to '2025/2026'...")
        year_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='year']")))
        year_dropdown.click()
        time.sleep(0.1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='2025/2026']"))).click()
        time.sleep(0.1)
        
        # 4. Start and End Dates
        print(f"-> Entering start date: '{json_data.get('tanggal_mulai', '')}'...")
        start_date_input = wait.until(EC.presence_of_element_located((By.ID, "start_date")))
        start_date_input.clear()
        start_date_input.send_keys(json_data.get("tanggal_mulai", ""))
        
        print(f"-> Entering end date: '{json_data.get('tanggal_selesai', '')}'...")
        end_date_input = wait.until(EC.presence_of_element_located((By.ID, "end_date")))
        end_date_input.clear()
        end_date_input.send_keys(json_data.get("tanggal_selesai", ""))
        time.sleep(0.1)

        # 5. EXECUTE CATEGORY & ACTIVITY DROPDOWNS
        click_dropdown(wait, driver, "category", json_data.get("jenis_kategori"))
        click_dropdown(wait, driver, "activity", json_data.get("jenis_kegiatan"))
        click_dropdown(wait, driver, "level", json_data.get("tingkat_kegiatan"))
        click_dropdown(wait, driver, "participation", json_data.get("keikutsertaan"))

        # 6. Description
        print("-> Writing description...")
        description_xpath = "//textarea[@formcontrolname='description']"
        description_input = wait.until(EC.presence_of_element_located((By.XPATH, description_xpath)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", description_input)
        time.sleep(0.1)
        description_input.clear()
        description_input.send_keys(json_data.get("deskripsi", ""))
        
        # 7. Upload Certificate File
        certificate_name = os.path.basename(pdf_path)
        print(f"-> Uploading certificate file: '{certificate_name}'...")
        file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        certificate_path = os.path.abspath(pdf_path) 
        file_input.send_keys(certificate_path)

        # 8. DROPDOWN FOR ORGANIZER TYPE (INTERNAL/EXTERNAL)
        click_dropdown(wait, driver, "organizer_type_id", json_data.get("jenis_penyelenggara"))

        # 9. Organizer
        print(f"-> Entering organizer: '{json_data.get('penyelenggara', '')}'...")
        organizer_input = wait.until(EC.presence_of_element_located((By.NAME, "organizer")))
        organizer_input.clear()
        organizer_input.send_keys(json_data.get("penyelenggara", ""))
        
        # 10. Activity Name
        print(f"-> Entering activity name: '{json_data.get('nama_kegiatan', '')}'...")
        act_name_input = wait.until(EC.presence_of_element_located((By.NAME, "activity_name_id")))
        act_name_input.clear()
        act_name_input.send_keys(json_data.get("nama_kegiatan", ""))
        
        # 11. English Activity Name
        print(f"-> Entering English activity name: '{json_data.get('nama_kegiatan_inggris', '')}'...")
        act_en_input = wait.until(EC.presence_of_element_located((By.NAME, "activity_name_en")))
        act_en_input.clear()
        act_en_input.send_keys(json_data.get("nama_kegiatan_inggris", ""))
        
        print("\nAll data and files have been successfully injected automatically!")
        print("Done! Please review the form in the browser and check the agreement statement before Submitting.")
        
    except Exception as e:
        print(f"A Selenium error occurred: {e}")
    finally:
        print("Finished filling out one form.")

def select_pdf_file():
    pdf_folder = "certificate_pdf"
    
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"\n[INFO] The '{pdf_folder}' folder has just been created!")
        print(f"Please move all your PDF files into the '{pdf_folder}' folder and re-run the script.")
        return None
        
    pdf_list = [file for file in os.listdir(pdf_folder) if file.lower().endswith('.pdf')]
    
    if not pdf_list:
        print(f"\nNo PDF files found in the '{pdf_folder}' folder.")
        return None
        
    print(f"\n=== CERTIFICATE FILE LIST (Inside '{pdf_folder}' folder) ===")
    for index, file in enumerate(pdf_list):
        full_path = os.path.join(pdf_folder, file)
        
        size_bytes = os.path.getsize(full_path)
        size_mb = size_bytes / (1024 * 1024)
        warning = " ⚠️ (EXCEEDS 2 MB!)" if size_mb > 2 else f" ({size_mb:.2f} MB)"
        print(f"[{index + 1}] {file}{warning}")
        
    while True:
        try:
            choice = int(input("\nEnter the number of the file you want to process: "))
            if 1 <= choice <= len(pdf_list):
                selected_file = pdf_list[choice - 1]
                full_path = os.path.join(pdf_folder, selected_file)
                
                size_bytes = os.path.getsize(full_path)
                if size_bytes > 2 * 1024 * 1024:
                    print(f"\n[X] REJECTED: The file size of '{selected_file}' is {size_bytes / (1024*1024):.2f} MB.")
                    print("Telkom's TAK web limits the maximum size to 2 MB. Please compress your PDF and try again.")
                    continue 
                    
                print(f"Selected file: {selected_file}\n")
                
                return full_path 
            else:
                print("Number out of range. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def auto_open_browser(choice):
    tak_url = "https://situ-kem.telkomuniversity.ac.id/tak/input-tak"
    is_mac = sys.platform == "darwin" 
    
    if choice == '1': # Microsoft Edge
        if is_mac:
            browser_path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
            data_dir = os.path.expanduser("~/edge_debug")
        else:
            browser_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            data_dir = r"C:\edge_debug"
            
    elif choice == '2': # Google Chrome
        if is_mac:
            browser_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            data_dir = os.path.expanduser("~/chrome_debug")
        else:
            browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            data_dir = r"C:\chrome_debug"
            
    elif choice == '3': # Brave Browser
        if is_mac:
            browser_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
            data_dir = os.path.expanduser("~/brave_debug")
        else:
            browser_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            data_dir = r"C:\brave_debug"
            
    elif choice == '4': # Opera Browser
        if is_mac:
            browser_path = "/Applications/Opera.app/Contents/MacOS/Opera"
            data_dir = os.path.expanduser("~/opera_debug")
        else:
            browser_path = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Opera\launcher.exe")
            data_dir = r"C:\opera_debug"
    else:
        return False

    if not os.path.exists(browser_path):
        if choice == '4' and not is_mac:
            browser_path = r"C:\Program Files\Opera\launcher.exe"
            if os.path.exists(browser_path):
                pass 
            else:
                print(f"\n[X] Failed: Cannot find Opera on this machine.")
                return False
        else:
            print(f"\n[X] Failed: Cannot find browser at '{browser_path}'")
            print("Make sure the browser is installed!")
            return False

    print("\nOpening browser in debugging mode...")
    subprocess.Popen([browser_path, "--remote-debugging-port=9222", f"--user-data-dir={data_dir}", tak_url])
    time.sleep(2) 
    return True

def initialize_browser():
    print("\n" + "-"*50)
    print("=== CHOOSE BROWSER ===")
    print("[1] Microsoft Edge")
    print("[2] Google Chrome")
    print("[3] Brave Browser")
    print("[4] Opera Browser")
    print("-"*50)
    
    while True:
        choice = input("Enter browser number: ").strip()
        
        if choice in ['1', '2', '3', '4']:
            if not auto_open_browser(choice):
                continue 
            
            try:
                if choice == '1':
                    print("Connecting to Microsoft Edge...")
                    options = EdgeOptions()
                    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    service = EdgeService(EdgeChromiumDriverManager().install())
                    return webdriver.Edge(service=service, options=options)
                    
                elif choice in ['2', '3', '4']:
                    browser_name = "Chrome" if choice == '2' else "Brave" if choice == '3' else "Opera"
                    print(f"Connecting to {browser_name}...")
                    options = ChromeOptions()
                    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    service = ChromeService(ChromeDriverManager().install())
                    return webdriver.Chrome(service=service, options=options)
                    
            except Exception as e:
                print(f"\n[FAILED] Cannot connect to the browser.")
                print(f"Error details: {e}")
                sys.exit(1)
        else:
            print("[X] Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_driver = initialize_browser()

    while True:
        print("\n" + "-"*50)
        pdf_file = select_pdf_file()
        
        if pdf_file:
            certificate_data = extract_certificate_to_json(pdf_file)
            if certificate_data:
                fill_tak_form(main_driver, certificate_data, pdf_file)
        else:
            print("Process skipped because no PDF file was selected.")
            
        print("\n" + "-"*50)
        repeat = input("Do you want to process another certificate? (y/n): ").strip().lower()
        
        if repeat != 'y':
            print("Thank you! Please click the cross (X) button in the top right corner to close this window.")
            break