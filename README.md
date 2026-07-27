# License Plate OCR menggunakan Visual Language Model (VLM)

## Deskripsi

Project ini melakukan Optical Character Recognition (OCR) pada plat nomor kendaraan Indonesia menggunakan Visual Language Model (VLM), yaitu **Qwen2.5-VL-7B**, yang dijalankan secara lokal melalui **LM Studio**.

Setiap gambar plat nomor dikirim ke model beserta prompt instruksi, model mengembalikan teks prediksi plat nomor, lalu hasilnya dibandingkan dengan ground truth menggunakan metrik **Character Error Rate (CER)**.

---

## Struktur Project

```text
src/
├── config.py           # Konfigurasi dataset, endpoint LM Studio, dan prompt
├── ground_truth.py      # Fungsi pembaca label ground truth
├── vlm_ocr.py           # Fungsi pemanggilan VLM untuk prediksi plat nomor
├── metrics.py            # Fungsi perhitungan CER
├── main.py               # Script utama untuk menjalankan seluruh pipeline
├── requirements.txt      # Daftar dependency Python
├── dataset/
│   ├── classes.names     # Daftar karakter yang dikenali (0-9, A-Z)
│   ├── image/             # Gambar plat nomor (.jpg)
│   └── ground-truth/      # Label teks plat nomor asli (.txt)
└── outputs/
    └── results.csv        # Hasil prediksi dan skor CER (dibuat otomatis)
```

---

## Requirements

Install dependency:

```bash
pip install -r requirements.txt
```

Dependency utama:

- `openai` — client untuk berkomunikasi dengan server LM Studio (kompatibel API OpenAI)
- `pandas` — menyusun dan menyimpan hasil ke CSV
- `numpy`
- `jiwer` — perhitungan Character Error Rate (CER)
- `tqdm` — progress bar

---

## Setup LM Studio

1. Install [LM Studio](https://lmstudio.ai/).
2. Download model **Qwen2.5-VL-7B-Instruct**.
3. Load model tersebut di LM Studio.
4. Jalankan **Local Server** (Developer → Start Server).

Endpoint default yang digunakan project ini:

```text
http://127.0.0.1:1234/v1
```

Pastikan endpoint dan nama model pada `config.py` sesuai dengan yang aktif di LM Studio:

```python
LMSTUDIO_URL = "http://127.0.0.1:1234/v1"
MODEL_NAME = "qwen/qwen2.5-vl-7b"
```

---

## Dataset

Dataset plat nomor Indonesia diletakkan di dalam folder `dataset/`, dengan format:

```text
dataset/
├── classes.names        # daftar karakter valid: 0-9 dan A-Z
├── image/                # file gambar, contoh: test001_1.jpg
└── ground-truth/         # file label teks, contoh: test001_1.txt
```

Setiap gambar memiliki pasangan file label dengan nama yang sama. Contoh isi file ground truth:

```text
B 9140 BCD
```

---

## Cara Menjalankan

Jalankan script utama dari dalam folder `src`:

```bash
python main.py
```

Program akan:

1. Membaca seluruh gambar pada `dataset/image/` (`.jpg`, `.jpeg`, `.png`).
2. Mengirim setiap gambar ke model VLM melalui LM Studio untuk diprediksi.
3. Membandingkan prediksi dengan ground truth menggunakan CER.
4. Menyimpan seluruh hasil ke `outputs/results.csv`.
5. Menampilkan rata-rata CER dan akurasi di terminal.

---

## Output

File hasil: `outputs/results.csv`

Format kolom:

```text
image, ground_truth, prediction, CER_score
```

Contoh:

```csv
image,ground_truth,prediction,CER_score
test001_1.jpg,B9140BCD,BS140BCD,0.125
test001_2.jpg,B2407UZO,B2407UZ0,0.125
test001_3.jpg,B2842PKM,B2842PKM,0.0
```

---

## Character Error Rate (CER)

CER dihitung menggunakan library `jiwer`, dengan konsep:

```
CER = (S + D + I) / N
```

Keterangan:

- **S** = jumlah substitusi karakter
- **D** = jumlah penghapusan (deletion) karakter
- **I** = jumlah penyisipan (insertion) karakter
- **N** = jumlah karakter pada ground truth

Semakin kecil nilai CER, semakin baik performa OCR. Akurasi ditampilkan sebagai `(1 - rata-rata CER) × 100%`.

---

## Alur Kerja (Workflow)

```text
Gambar Plat Nomor
        ↓
  Qwen2.5-VL (via LM Studio)
        ↓
   Teks Prediksi
        ↓
  Evaluasi CER (vs Ground Truth)
        ↓
   outputs/results.csv
```

---

## Catatan

- Semua gambar diproses satu per satu (sekuensial), sehingga waktu proses tergantung kecepatan inferensi model di LM Studio.
- Jika terjadi error saat memproses satu gambar (misalnya server LM Studio tidak aktif), gambar tersebut tetap dicatat pada `results.csv` dengan prediksi kosong dan skor `None`, agar proses tidak terhenti.
- Prompt yang dikirim ke model dapat disesuaikan di `config.py` pada variabel `PROMPT`.

---

## Author

Computer Vision Final Project
Robotics Engineering
