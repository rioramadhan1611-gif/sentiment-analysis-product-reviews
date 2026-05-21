📊 Sentiment Analysis — Product Reviews
Proyek analisis sentimen ulasan produk skincare menggunakan Python dan TextBlob. Dibuat sebagai bagian dari portofolio data science.

🎯 Tujuan
Mengklasifikasikan ulasan pelanggan secara otomatis menjadi Positif, Negatif, atau Netral untuk membantu tim marketing memahami persepsi pelanggan terhadap produk.

📁 Struktur Proyek
project-sentimen/
│
├── buat_data.py            ← generate dataset simulasi
├── 01_eksplorasi.py        ← eksplorasi & pemahaman data
├── 02_preprocessing.py     ← pembersihan teks
├── 03_analisis.py          ← klasifikasi sentimen
├── 04_visualisasi.py       ← visualisasi hasil
│
├── ulasan.csv              ← data mentah
├── ulasan_bersih.csv       ← data setelah preprocessing
└── ulasan_hasil.csv        ← data hasil analisis
🛠️ Tools & Library
Library	Fungsi
Pandas	Pengolahan dan analisis data
TextBlob	Analisis sentimen teks
Matplotlib	Visualisasi data
Re	Preprocessing teks (regex)
📊 Hasil Analisis
Sentimen	Jumlah	Persentase
Positif	13 ulasan	65%
Negatif	5 ulasan	25%
Netral	2 ulasan	10%
💡 Insight
Sunscreen SPF 50 memiliki skor sentimen tertinggi di antara semua produk
65% ulasan pelanggan bersifat positif — indikator kepuasan yang baik
Rating bintang tinggi berkorelasi dengan sentimen positif
Kata yang paling sering muncul di ulasan positif: product, skin, good, feel
TextBlob memiliki keterbatasan dalam memahami konteks — ulasan dengan kata "wonders" mendapat skor netral meskipun positif secara makna
⚙️ Cara Menjalankan
1. Clone repository
git clone https://github.com/USERNAME_KAMU/sentiment-analysis-product-reviews.git

2. Install dependencies
pip install pandas textblob matplotlib

3. Download data TextBlob
python -m textblob.download_corpora

4. Jalankan file secara berurutan
python buat_data.py python 01_eksplorasi.py python 02_preprocessing.py python 03_analisis.py python 04_visualisasi.py

📈 Visualisasi
Distribusi Sentimen
Pie Chart

Sentimen per Produk
Bar Chart

Skor Sentimen per Produk
Skor

Kata Paling Sering di Ulasan Positif
Kata Positif

👤 Author
Rio Ramadhan — Mahasiswa Manajemen Pemasaran yang tertarik di bidang Data Science
📧 rioramadhan1611@gmail.com. 🔗 LinkedIn
