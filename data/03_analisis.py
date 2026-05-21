# ================================================
# TAHAP 3 - ANALISIS SENTIMEN
# ================================================
import pandas as pd
from textblob import TextBlob

df = pd.read_csv("ulasan_bersih.csv")

# ================================================
# BAGIAN 1 - Cara Kerja Textblob
# ================================================
print("=== Cara Kerja Textblob ===")

contoh = TextBlob("This product is absolutely amazing and wonderful")
print(f"Teks : {contoh}")
print(f"Polarity: {contoh.sentiment.polarity}")
# Polarity = angka dari -1.0 sampai 1.0
# -1.0 = sangat negatif
#  0.0 = netral
# +1.0 = sangat positif

contoh2= TextBlob("This product is terrible and very disappointing")
print(f"\nTeks : {contoh2}")
print(f"Polarity: {contoh2.sentiment.polarity}")

# ============================================
# BAGIAN 2 — Fungsi klasifikasi sentimen
# ============================================
def analisis_sentimen(teks):
    skor = TextBlob(teks).sentiment.polarity
    if skor > 0.1:
        return "Positif"
    elif skor < -0.1:
        return "Negatif"
    else:
        return "Netral"

def ambil_skor(teks):
    return round(TextBlob(teks).sentiment.polarity,3)

# ============================================
# BAGIAN 3 — Terapkan ke semua ulasan
# ============================================
df["sentimen"]      = df["ulasan_bersih"].apply(analisis_sentimen)
df["skor_sentimen"] = df["ulasan_bersih"].apply(ambil_skor)

# ============================================
# BAGIAN 4 — Tampilkan hasil
# ============================================
print("\n=== HASIL ANALISIS SENTIMEN ===")
for i, row in df.iterrows():
    print(f"\n{row['nama_produk']}")
    print(f"    Ulasan      : {row['ulasan'][:50]}...")
    print(f"    skor        : {row['skor_sentimen']}")
    print(f"    Sentimen    : {row['sentimen']}")

# ============================================
# BAGIAN 5 — Ringkasan
# ============================================
print("\n=== RINGKASAN SENTIMEN ===")
distribusi = df["sentimen"].value_counts()
total     = len(df)

for sentimen, jumlah in distribusi.items():
    persen = round(jumlah/total * 100,1)
    print(f"{sentimen:10} : {jumlah} ulasan ({persen}%)")

print("\n=== RATA-RATA SKOR PER PRODUK ===")
rata_produk = df.groupby("nama_produk")["skor_sentimen"].mean().round(3)
print(rata_produk.sort_values(ascending=False))

print("\n=== KORELASI SENTIMEN VS RATING BINTANG ===")
print(df.groupby("sentimen")["rating_bintang"].mean().round(2))

# --- Simpan hasil ---
df.to_csv("ulasan_hasil.csv", index=False)
print("\nHasil tersimpan di ulasan_hasil.csv")