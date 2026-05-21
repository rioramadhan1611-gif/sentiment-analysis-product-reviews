# ============================================
# TAHAP 4 — VISUALISASI HASIL SENTIMEN
# ============================================
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("ulasan_hasil.csv")

# ============================================
# GRAFIK 1 — Pie chart distribusi sentimen
# ============================================
distribusi = df["sentimen"].value_counts()

plt.figure(figsize= (7,7))
plt.pie(
distribusi.values,
    labels=distribusi.index,
    autopct="%1.1f%%",
    colors=["#2ecc71", "#e74c3c", "#95a5a6"],  # hijau, merah, abu
    startangle=90
)
plt.title("Distribusi Sentimen Ulasan Produk")
plt.tight_layout()
plt.savefig("grafik_sentimen_pie.png")
plt.show()

# ============================================
# GRAFIK 2 — Bar chart sentimen per produk
# ============================================
sentimen_produk = df.groupby(
    ["nama_produk", "sentimen"]
).size().unstack(fill_value=0)

sentimen_produk.plot(
    kind="bar",
    figsize=(10, 6),
    color=["#e74c3c", "#95a5a6", "#2ecc71"],  # negatif, netral, positif
    width=0.7
)

plt.title("Distribusi Sentimen per Produk")
plt.xlabel("Nama Produk")
plt.ylabel("Jumlah Ulasan")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Sentimen")
plt.tight_layout()
plt.savefig("grafik_sentimen_produk.png")
plt.show()

# ============================================
# GRAFIK 3 — Bar chart rata-rata skor sentimen
# ============================================
rata_skor = df.groupby("nama_produk")["skor_sentimen"].mean().sort_values()

warna = ["#e74c3c" if x < 0 else "#2ecc71" for x in rata_skor.values]

plt.figure(figsize=(10, 5))
plt.bar(rata_skor.index, rata_skor.values, color=warna)
plt.axhline(y=0, color="black", linewidth=0.8, linestyle="--")
plt.title("Rata-rata Skor Sentimen per Produk")
plt.xlabel("Nama Produk")
plt.ylabel("Skor Sentimen (-1 hingga +1)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafik_skor_sentimen.png")
plt.show()

# ============================================
# GRAFIK 4 — Kata paling sering di ulasan positif
# ============================================
from collections import Counter

teks_positif = " ".join(
    df[df["sentimen"] == "Positif"]["ulasan_bersih"].values
)

kata_list = teks_positif.split()
frekuensi = Counter(kata_list)
top_kata  = pd.DataFrame(
    frekuensi.most_common(15),
    columns=["kata", "jumlah"]
)

plt.figure(figsize=(10, 6))
plt.barh(top_kata["kata"], top_kata["jumlah"], color="seagreen")
plt.title("15 Kata Paling Sering di Ulasan Positif")
plt.xlabel("Jumlah Kemunculan")
plt.ylabel("Kata")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("grafik_kata_positif.png", dpi=200)
plt.show()

# ============================================
# GRAFIK 5 — Word cloud ulasan positif (versi rapi)
# ============================================
teks_positif = " ".join(
    df[df["sentimen"] == "Positif"]["ulasan_bersih"].values
)

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white",
    colormap="RdYlGn",         # gradasi merah-kuning-hijau
    max_words=50,
    max_font_size=120,         # ukuran font terbesar
    min_font_size=14,          # ukuran font terkecil
    prefer_horizontal=0.9,     # 90% kata horizontal, 10% vertikal
    margin=10,                 # jarak antar kata
    collocations=False         # hindari kata ganda yang berulang
).generate(teks_positif)

plt.figure(figsize=(14, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

# Tambah judul yang lebih rapi
plt.title(
    "Kata yang Sering Muncul di Ulasan Positif",
    fontsize=16,
    fontweight="bold",
    pad=20
)

# Tambah border tipis di sekitar gambar
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

plt.tight_layout(pad=2)
plt.savefig("grafik_wordcloud_positif.png", dpi=200, bbox_inches="tight")
plt.show()