# ===========================================
# TAHAP 2 - PRE-PROCESSING
# ===========================================

import pandas as pd
import re

df = pd.read_csv('ulasan.csv')

print("=== TEKS ASLI (SEBELUM DI BERSIHKAN) ===")
print(df["ulasan"][0])

# --- Fungsi pembersih ---
def bersihkan_teks(teks):
    teks = teks.lower()
    teks = re.sub(r'[^a-z\s]', '',teks)
    teks = teks.strip()
    return teks

# --- Terapkan ke Seluruh Ulasan ---
df["ulasan_bersih"] = df["ulasan"].apply(bersihkan_teks)

print("\n=== TEKS SETELAH DIBERSIHKAN ===")
print(df["ulasan_bersih"][0])

print("\n=== PERBANDINGAN SEBELUM DAN SESUDAH")
for i in range(3):
    print(f"\nUlasan {i+1} asli : {df['ulasan'][i]}")
    print(f"\nUlasan {i+1} bersih : {df['ulasan_bersih'][i]}")

# --- Simpan Data yang Sudah Bersih ---
df.to_csv("ulasan_bersih.csv", index=False)
print("\nData bersih tersimpan di ulasan_bersih.csv")