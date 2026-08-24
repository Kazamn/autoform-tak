const REFERENSI_DROPDOWN = `
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
`;

const SYSTEM_PROMPT = `
You are an automated data extraction system for filling out the Telkom University Transkrip Aktivitas Kemahasiswaan (TAK) form.
Here is the reference for the available dropdown options in the system:
${REFERENSI_DROPDOWN}

Comply with the following JSON key structure and ensure the categories use the exact text from the reference:
- "tanggal_selesai": (Format WAJIB DD/MM/YYYY. Contoh: 05/08/2026)
- "tanggal_mulai": (Format WAJIB DD/MM/YYYY. ATURAN LOGIKA WAKTU: Jika durasi sertifikat < 24 jam, tanggal_mulai = tanggal_selesai. TETAPI, jika durasi >= 24 jam, wajib HITUNG MUNDUR dari tanggal_selesai dengan asumsi 1 hari = 12 jam belajar. Contoh: Jika selesai 20/08/2026 dan durasi 90 jam, maka outputkan tanggal_mulai menjadi 12/08/2026 atau 13/08/2026.)
- "deskripsi": (1-2 kalimat bahasa Indonesia. ATURAN MUTLAK: 1. JANGAN PERNAH memasukkan nama peserta ke dalam deskripsi. 2. Jika durasi < 12 jam, JANGAN sebutkan info angka waktu/durasi sama sekali. Jika durasi >= 12 jam, sebutkan durasinya dan wajib gunakan kata 'estimasi'.)
- "penyelenggara": (Nama Institusi)
- "nama_kegiatan": (Judul kegiatan)
- "nama_kegiatan_inggris": (Translate ke Inggris)
- "jenis_kategori": (RULE: Jika sertifikat online course, WAJIB pilih "Pelatihan")
- "jenis_kegiatan": (Pilih satu yang tepat)
- "tingkat_kegiatan": (Evaluasi skala kegiatan secara cerdas dan mandiri. Analisis konteks dari nama acara, penyelenggara, dan bahasa yang digunakan. Tentukan apakah skala acara ini "Internasional", "Nasional", "Regional", atau "Universitas". CATATAN: Sebuah acara bisa saja berskala "Internasional" (seperti summit/konferensi global) meskipun diselenggarakan secara fisik di Indonesia. Gunakan pengetahuan umum dan logikamu untuk menilai skala sesungguhnya dari acara tersebut.)
- "keikutsertaan": (Pilih satu yang tepat)
- "jenis_penyelenggara": (Internal atau External)

Output ONLY pure JSON without markdown.
`;

// 1. Load & Save API Key
document.addEventListener('DOMContentLoaded', () => {
    chrome.storage.local.get(['geminiApiKey'], (result) => {
        if (result.geminiApiKey) document.getElementById('apiKey').value = result.geminiApiKey;
    });

    document.getElementById('saveKeyBtn').addEventListener('click', () => {
        const key = document.getElementById('apiKey').value;
        chrome.storage.local.set({ geminiApiKey: key }, () => {
            const status = document.getElementById('status');
            status.innerText = "API Key Saved Securely!";
            status.style.color = "#2ea043";
        });
    });

    // 2. Main Logic
    document.getElementById('processBtn').addEventListener('click', async () => {
        const apiKey = document.getElementById('apiKey').value;
        const fileInput = document.getElementById('pdfFile');
        const statusEl = document.getElementById('status');

        if (!apiKey) return statusEl.innerText = "Error: Please enter your Gemini API Key!";
        if (!fileInput.files.length) return statusEl.innerText = "Error: Please select a PDF file!";

        const file = fileInput.files[0];
        
        if (file.size > 2 * 1024 * 1024) {
            statusEl.innerText = "Error: File max 2 MB!";
            statusEl.style.color = "#ff3333";
            return;
        }

        const reader = new FileReader();

        reader.onload = async function(e) {
            const base64Data = e.target.result.split(',')[1];
            const fileName = file.name;
            const fileMimeType = file.type;
            let finalJsonData = null;
            let successModelName = "";

            // --- FALLBACK MODEL (3.7 -> 3.6 -> 3.5 -> ...) ---
            const modelList = [
                "gemini-3.7-flash",
                "gemini-3.6-flash",
                "gemini-3.5-flash",
                "gemini-3.1-pro-preview",
                "gemini-pro-latest",        
                "gemini-3-flash-preview",
                "gemini-3.5-flash-lite",    
                "gemini-3.1-flash-lite",     
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",     
                "gemini-2.5-pro",
                "gemini-flash-latest"       
            ];

            for (const modelName of modelList) {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 15000);

                try {
                    statusEl.innerText = `Analyzing document using ${modelName}`;
                    statusEl.style.color = "#4daafc";
                    
                    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${apiKey}`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        signal: controller.signal, 
                        body: JSON.stringify({
                            contents: [{
                                parts: [
                                    { text: SYSTEM_PROMPT },
                                    { inline_data: { mime_type: fileMimeType, data: base64Data } }
                                ]
                            }]
                        })
                    });

                    clearTimeout(timeoutId);

                    const data = await response.json();
                    if (!response.ok) throw new Error(data.error?.message || `Failed with ${modelName}`);

                    let textResult = data.candidates[0].content.parts[0].text.trim();
                    textResult = textResult.replace(/```json/g, "").replace(/```/g, "").trim();
                    finalJsonData = JSON.parse(textResult);
                    successModelName = modelName;
                    break; 

                } catch (error) {
                    clearTimeout(timeoutId);
                    
                    if (error.name === 'AbortError') {
                        console.warn(`[!] ${modelName} timeout (>15 detik). Switching to next model...`);
                    } else {
                        console.warn(`[!] ${modelName} failed. Switching to next model...`, error);
                    }
                }
            }

            try {
                statusEl.innerText = `Data from ${successModelName} ready! Injecting`;

                let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
                
                await chrome.scripting.executeScript({
                    target: { tabId: tab.id },
                    func: injectFormData,
                    args: [finalJsonData, base64Data, fileName, fileMimeType]
                });

                statusEl.innerText = "Success! Please review before submit.";
                statusEl.style.color = "#2ea043";

            } catch (error) {
                console.error(error);
                statusEl.innerText = "Injection Failed: " + error.message;
                statusEl.style.color = "#ff3333";
            }
        };
        reader.readAsDataURL(file);
    });
});

async function injectFormData(jsonData, base64Pdf, fileName, fileMimeType) {
    const delay = ms => new Promise(res => setTimeout(res, ms));

    console.log("[AUTOFORM] Start Injection Data", jsonData);

    jsonData.tanggal_mulai = jsonData.tanggal_mulai.trim();
    jsonData.tanggal_selesai = jsonData.tanggal_selesai.trim();

    if (jsonData.tanggal_mulai.includes("01/01/2025") || jsonData.tanggal_mulai.includes("2025")) {
        console.warn("⚠️ [AUTOFORM] Menimpa tanggal mulai secara paksa!");
        jsonData.tanggal_mulai = jsonData.tanggal_selesai;
    }

    // 1. Native Setter Hack
    function fillText(selector, value) {
        let el = document.querySelector(selector);
        if (el && value) {
            el.focus(); 
            let nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            let nativeTextAreaValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
            
            if (el.tagName.toLowerCase() === 'textarea') {
                nativeTextAreaValueSetter.call(el, value);
            } else {
                nativeInputValueSetter.call(el, value);
            }
            
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
            el.blur(); 
        }
    }

    // 2. Dropdown Angular
    async function clickDropdown(formControlName, targetText) {
        if (!targetText || targetText === "-") return;
        
        console.log(`[AUTOFORM] Waiting dropdown '${formControlName}' ready`);
        let dropdown = null;
        for(let i = 0; i < 25; i++) {
            dropdown = document.querySelector(`ng-select[formcontrolname="${formControlName}"]`);
            if (dropdown && !dropdown.classList.contains('ng-select-disabled')) break;
            await delay(200); 
        }

        if (!dropdown || dropdown.classList.contains('ng-select-disabled')) return;

        let clickArea = dropdown.querySelector('.ng-select-container') || dropdown.querySelector('.single') || dropdown;
        clickArea.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
        clickArea.click(); 

        let optionToClick = null;
        for (let i = 0; i < 20; i++) {
            await delay(200); 
            let options = Array.from(document.querySelectorAll(`ng-dropdown-panel .ng-option, select-dropdown li`));
            
            optionToClick = options.find(opt => {
                let optText = opt.innerText.trim().toLowerCase();
                let tgtText = targetText.trim().toLowerCase();
                if (optText === tgtText) return true;
                if (optText.includes(tgtText)) {
                    if (tgtText === "nasional" && optText.includes("internasional")) return false;
                    return true;
                }
                return false;
            });
            if (optionToClick) break; 
        }

        if (optionToClick) {
            optionToClick.click(); 
        } else {
            document.body.click(); 
        }
        await delay(800); 
    }

    await clickDropdown("year", "2025/2026");
    await clickDropdown("category", jsonData.jenis_kategori);
    await clickDropdown("activity", jsonData.jenis_kegiatan);
    await clickDropdown("level", jsonData.tingkat_kegiatan);
    await clickDropdown("participation", jsonData.keikutsertaan);
    await clickDropdown("organizer_type_id", jsonData.jenis_penyelenggara);

    fillText('#start_date', jsonData.tanggal_mulai);
    fillText('#end_date', jsonData.tanggal_selesai);
    fillText('textarea[formcontrolname="description"]', jsonData.deskripsi);
    fillText('input[name="organizer"]', jsonData.penyelenggara);
    fillText('input[name="activity_name_id"]', jsonData.nama_kegiatan);
    fillText('input[name="activity_name_en"]', jsonData.nama_kegiatan_inggris);

    const fileInput = document.querySelector("input[type='file']");
    if (fileInput && base64Pdf) {
        const byteCharacters = atob(base64Pdf);
        const byteNumbers = new Array(byteCharacters.length);
        for (let i = 0; i < byteCharacters.length; i++) byteNumbers[i] = byteCharacters.charCodeAt(i);
        
        const blob = new Blob([new Uint8Array(byteNumbers)], { type: fileMimeType });
        const file = new File([blob], fileName, { type: fileMimeType });

        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;
        fileInput.dispatchEvent(new Event('change', { bubbles: true }));
    }
    
    console.log("[AUTOFORM] All Process Finished");
}