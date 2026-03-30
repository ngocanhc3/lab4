"""
Bai 5 - Tong hop va so sanh hai mien linh vuc
So sanh Bai 1 (Giao duc) va Bai 3 (Kinh doanh)
"""

import numpy as np

print("="*70)
print("BAI 5: TONG HOP VA SO SANH HAI MIEN LINH VUC")
print("="*70)

print("\nChon so sanh: Bai 1 (Phan tich diem hoc phan) - Mien GIAO DUC")
print("               Bai 3 (Phan tich doanh thu) - Mien KINH DOANH")

# ============== Du lieu tu Bai 1 ==============
print("\n" + "="*70)
print("DU LIEU BAI 1: PHAN TICH DIEM HOC PHAN")
print("="*70)

scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

print(f"Ma tran shape: {scores.shape}")
print(f"  - So sinh vien: {scores.shape[0]}")
print(f"  - So cot diem: {scores.shape[1]} (chuyen can, giua ky, thuc hanh, cuoi ky)")

# ============== Du lieu tu Bai 3 ==============
print("\n" + "="*70)
print("DU LIEU BAI 3: PHAN TICH DOANH THU")
print("="*70)

sales = np.array([
    [120, 150, 130, 140, 160],
    [125, 145, 128, 142, 158],
    [130, 155, 135, 150, 162],
    [135, 160, 140, 152, 168],
    [140, 165, 145, 155, 170],
    [138, 162, 142, 153, 169],
    [145, 170, 150, 160, 175]
])

print(f"Ma tran shape: {sales.shape}")
print(f"  - So ngay (hang): {sales.shape[0]}")
print(f"  - So san pham (cot): {sales.shape[1]}")

# ============== CAU HOI 1 ==============
print("\n" + "="*70)
print("CAU HOI 1: DU LIEU CO GIONG NHAU VE CAU TRUC?")
print("="*70)

print("""
DIEM GIONG NHAU VE CAU TRUC:

1. Ca hai deu la ma tran 2D:
   - Bai 1: 10 sinh vien x 4 thanh phan diem (10x4)
   - Bai 3: 7 ngay x 5 san pham (7x5)

2. Ca hai co y nghia "theo doi nhieu doi tuong qua nhieu tieu chi":
   - Bai 1: Theo doi diem cua moi sinh vien o 4 thanh phan
   - Bai 3: Theo doi doanh thu cua 5 san pham trong 7 ngay

3. Ca hai su dung dtype float/numeric de luu tru du lieu dinh luong

4. Ca hai co "chieu thu nhat" la cac doi tuong rieng le:
   - Sinh vien, san pham
   - Va "chieu thu hai" la cac tieu chi/thoi gian

5. Muc tieu phan tich tuong tu nhau:
   - Bai 1: Tinh toan chi so tong hop (diem tong ket)
   - Bai 3: Tinh toan chi so tong hop (doanh thu tong)
""")

# ============== CAU HOI 2 ==============
print("\n" + "="*70)
print("CAU HOI 2: PHEP TOAN NUMPY NAO DUOC DUNG O CA HAI BAI?")
print("="*70)

print("""
CAC PHEP TOAN COMMON (DUOC DUNG O CA HAI BAI):

1. np.sum() / .sum():
   - Bai 1: Cong diem tu 4 cot -> diem tong ket
   - Bai 3: Cong doanh thu tu 7 ngay hoac 5 san pham

2. np.mean() / .mean():
   - Bai 1: Tinh diem trung binh, Z-score normalization
   - Bai 3: Tinh doanh thu trung binh

3. np.std() / .std():
   - Bai 1: Tinh do lech chuan cho Z-score chuan hoa
   - Bai 3: Tinh do lech chuan tim san pham on dinh

4. np.max() / np.min() / .max() / .min():
   - Bai 1: Tim sinh vien cao nhat/thap nhat
   - Bai 3: Tim ngay cao nhat, san pham ban tot nhat

5. np.argmax() / np.argmin():
   - Bai 1: Lay index sinh vien tot nhat
   - Bai 3: Lay index ngay/san pham tot nhat

6. np.where():
   - Bai 1: Tim sinh vien bi canh bao, co diem duoi 5.0
   - Bai 3: Tim ngay co doanh thu cao

7. np.any():
   - Bai 1: Kiem tra neu diem nao duoi 5.0
   - Bai 3: Kiem tra dieu kien tren cac phan tu

8. np.maximum() va np.clip():
   - Bai 4 (giong cau truc): Tinh luong nhap va gioi han gia tri
""")

# Demo
print("\n" + "-"*70)
print("VI DU CU THE:")
print("-"*70)

weights = np.array([0.1, 0.2, 0.3, 0.4])

final_score = scores @ weights
daily_total = sales.sum(axis=1)

print(f"Bai 1 - Phep toan @: scores @ weights = {final_score[:3]}...")
print(f"Bai 3 - Phep toan .sum(axis=1): {daily_total}...")
print(f"Ca hai dung .mean(), .std(), .max(), .min()")

# ============== CAU HOI 3 ==============
print("\n" + "="*70)
print("CAU HOI 3: BAI NAO DUNG BOOLEAN INDEXING NHIEU HON? VI SAO?")
print("="*70)

print("""
PHAN TICH SU DUNG BOOLEAN INDEXING:

Bai 1: Su dung rat nhieu boolean indexing
   1. Loc sinh vien co diem >= 7.0: final_score >= 7.0
   2. Phat hien sinh vien co diem duoi 5.0: np.any(scores < 5.0, axis=1)
   3. Xep loai: score >= 8.5, score >= 7.0, etc.
   4. Z-score analysis: z_scores > 1, z_scores < -1

Bai 3: Su dung it boolean indexing hon
   1. Loc ngay cao nhat: daily_total > daily_total.mean()
   2. So sanh doanh thu voi trung binh
   3. Gioi han: np.clip() khong phai boolean indexing

CONCLUSION: Bai 1 dung nhieu hon

VI SAO?
   - Bai 1 (Giao duc): Can phan loai, xep hang, canh bao -> nhieu dieu kien
   - Bai 3 (Kinh doanh): Chu yeu aggregation -> it dieu kien
   - Bai 1 co tinh "quan ly" cao (canh bao sinh vien) -> can loc du lieu
   - Bai 3 tap trung "phan tich xu huong" -> it can loc
""")

# ============== CAU HOI 4 ==============
print("\n" + "="*70)
print("CAU HOI 4: LOI ICH CUA VECTORIZATION SO VOI VONG LAP?")
print("="*70)

print("""
LOI ICH CUA VECTORIZATION:

1. HIEU SUAT CAO HON (10-100x nhanh hon):
   - Vong lap Python: Chap vi interpreted language
   - NumPy: Dung C code -> rat nhanh

2. CODE NGAN GON:
   - final_score = scores @ weights (1 dong)
   - vs: for i in range(n): final_score[i] = sum(...) (nhieu dong)

3. BO NHO HIEU QUA:
   - NumPy arrays luu tru lien tiep trong bo nho
   - Cache locality tot, it tao object tam thoi

4. TRANH LOI LOGIC PHUC TAP:
   - Khong can lo off-by-one errors, initialization, etc.

5. LINH HOAT VOI DIMENSIONALITY:
   - Hoat dong voi tensor bat ky
   - Vong lap phai thay doi theo so chieu
""")

import time

# Benchmark
start = time.time()
for _ in range(1000):
    result = scores @ weights
vector_time = time.time() - start

start = time.time()
for _ in range(1000):
    result = np.zeros(len(scores))
    for i in range(len(scores)):
        for j in range(len(weights)):
            result[i] += scores[i, j] * weights[j]
loop_time = time.time() - start

print(f"\nBenchmark (1000 lan):")
print(f"Vectorized (@): {vector_time*1000:.2f} ms")
print(f"Loop approach:  {loop_time*1000:.2f} ms")
print(f"Tang toc: {loop_time/vector_time:.1f}x lan")

# ============== CAU HOI 5 =================
print("\n" + "="*70)
print("CAU HOI 5: TANG 100 LAN, NUMPY HO TRO GI?")
print("="*70)

print("""
NUMPY HO TRO SCALABILITY:

1. Advanced Indexing:
   - Fancy indexing, boolean indexing, multi-dimensional indexing
   - Xu ly 1M sinh vien van nhanh

2. Phep toan nhanh:
   - Tinh toan tren mang nguyen, khong loop
   - Cache-friendly operations

3. Memory Mapping:
   - Doc file lon hon RAM vao memory efficiently
   - np.load('file.npy', mmap_mode='r')

4. Broadcasting:
   - Keo dan mang nho de match kich thuoc lon
   - Khong can copy du lieu

5. DTYPE Optimization:
   - float32 thay vi float64 -> tiet kiem RAM
   - Voi 1M phan tu: tiet kiem 4MB

6. Parallel Processing:
   - NumPy + Numba: JIT compile
   - NumPy + CuPy: GPU acceleration
   - NumPy + Dask: Parallel computing

7. Slicing va Chunking:
   - Chia du lieu lon thanh chunks nho
   - Xu ly tung chunk roi ket hop

8. Efficient Sorting:
   - np.argsort(), np.searchsorted() -> O(n log n)
   - Xep hang 1M sinh vien trong giay

Scalability:
  - 10x du lieu -> khoang 10x thoi gian (linear)
  - 100x du lieu -> khoang 100x thoi gian
  - Voi GPU: 1000x lan nhanh hon
  - 1M sinh vien x 100 thuoc tinh -> 1-2 giay
""")

# ============== TONG KET ==============
print("\n" + "="*70)
print("TOM TAT SO SANH")
print("="*70)

print("""
+========================+=====================+=====================+
| Tieu chi               | Bai 1 (Giao duc)    | Bai 3 (Kinh doanh)   |
+========================+=====================+=====================+
| Shape                  | (10, 4)             | (7, 5)              |
| Axis 0 (Hang)          | Sinh vien           | Ngay                |
| Axis 1 (Cot)           | 4 thanh phan diem   | 5 san pham          |
| Phep aggregation       | matrix mult + sum   | sum axis            |
| Boolean indexing       | NHIEU (phan loai)   | IT (aggregation)    |
| Tinh phan hoa          | Cao (std, z-score)  | Vua phai (std)      |
| Muc tieu                | Quan ly/Canh bao    | Xu huong/Quy hoach  |
+========================+=====================+=====================+

PHAT HIEN CHUNG:
1. Ca hai la bai toan "analytics" dien hinh
2. NumPy la cong cu hoan hao cho loai nay
3. Vectorization giup tang toc 10-100x
4. Boolean indexing la ky nang then chot
5. Phan tich du lieu lon can hieu scalability

KET LUAN:
- Bai 1: Tap trung QUAN LY (phan loai, xep hang, canh bao)
- Bai 3: Tap trung PHAN TICH (xu huong, so sanh, quy hoach)
- Hai bai toi uu khi dung NumPy vectorization
- Boolean indexing QUAN TRONG trong Bai 1
- Khi tang 100x, NumPy van xu ly hieu qua
""")

