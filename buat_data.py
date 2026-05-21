# ============================================
# BUAT DATA SIMULASI ULASAN PRODUK
# ============================================
import pandas as pd

data = {
    "id_ulasan": range(1, 21),
    "nama_produk": [
        "Serum Vitamin C", "Serum Vitamin C", "Serum Vitamin C", "Serum Vitamin C",
        "Pelembab Aloe Vera", "Pelembab Aloe Vera", "Pelembab Aloe Vera", "Pelembab Aloe Vera",
        "Sunscreen SPF 50", "Sunscreen SPF 50", "Sunscreen SPF 50", "Sunscreen SPF 50",
        "Toner Niacinamide", "Toner Niacinamide", "Toner Niacinamide", "Toner Niacinamide",
        "Eye Cream Retinol", "Eye Cream Retinol", "Eye Cream Retinol", "Eye Cream Retinol"
    ],
    "ulasan": [
        "This serum is absolutely amazing, my skin feels so bright and smooth",
        "Great product, very effective and the texture is lightweight",
        "Not bad but a little expensive for the size",
        "Terrible product, caused breakout on my skin, very disappointed",
        "Love this moisturizer, very hydrating and smells great",
        "Good product, skin feels soft after using it",
        "The texture is too thick, not suitable for oily skin",
        "Excellent moisturizer, best product I have ever used",
        "This sunscreen is perfect, no white cast and very lightweight",
        "Great sun protection, love how it feels on my skin",
        "Average product, does the job but nothing special",
        "Horrible smell and leaves white cast, waste of money",
        "This toner works wonders, pores look smaller after one week",
        "Very refreshing and hydrating, will definitely repurchase",
        "Okay product but took too long to see results",
        "Did not work for me at all, skin feels dry after using",
        "Amazing eye cream, dark circles reduced significantly",
        "Good product but the packaging is not practical",
        "Fantastic results after two weeks, highly recommend",
        "Too expensive and did not see any visible results"
    ],
    "rating_bintang": [5, 5, 3, 1, 5, 4, 2, 5, 5, 5, 3, 1, 5, 5, 3, 2, 5, 4, 5, 1]
}

df = pd.DataFrame(data)

import os
os.makedirs("data", exist_ok=True)   # ← buat folder data otomatis kalau belum ada

df.to_csv("data/ulasan.csv", index=False)
print(f"Data berhasil dibuat — {len(df)} ulasan tersimpan di data/ulasan.csv")