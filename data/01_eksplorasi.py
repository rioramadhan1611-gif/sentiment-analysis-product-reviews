# ============================================
# Tahap 1 - Eksplorasi Data
# ============================================

# Import library yang diperlukan
import pandas as pd

df= pd.read_csv("ulasan.csv")

print("=== SEKILAS DATA ===")
print(df.head())

print("=== INFORMASI DATA ===")
print(df.info())

print("=== CEK DATA KOSONG ===")
print(df.isnull().sum())

print("=== STATISTIK RATING BINTANG ===")
print(df['rating_bintang'].describe().round(2))  

print ("=== DISTRIBUSI RATING BINTANG ===")
distribusi = df['rating_bintang'].value_counts().sort_index()
for bintang, jumlah in distribusi.items():
    bintang_simbol = '⭐' * bintang
    print(f"{bintang_simbol}: {jumlah} ulasan") 

print("\n=== JUMLAH ULASAN PER PRODUK  ===")
print(df['nama_produk'].value_counts())