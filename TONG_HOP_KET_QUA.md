# TÓNG HỢP KẾT QUẢ CÁC BÀI TẬP LAB 4

## 🎯 TỔNG QUAN

Bộ bài tập LAB 4 gồm **5 bài** sử dụng NumPy để phân tích dữ liệu thực tế, được chia thành:
- **Miền Giáo dục:** Bài 1 (Điểm) & Bài 2 (Chuyên cần)
- **Miền Kinh doanh:** Bài 3 (Doanh thu) & Bài 4 (Tồn kho)
- **So sánh tổng hợp:** Bài 5 (Khái quát 2 miền)

---

## 📊 BÀI 1: PHÂN TÍCH ĐIỂM HỌC PHẦN

### Input
- 10 sinh viên, 4 thành phần điểm (chuyên cần, giữa kỳ, thực hành, cuối kỳ)
- Trọng số: 10%, 20%, 30%, 40%

### Output Chính
```
Shape: (10, 4)  |  Ndim: 2  |  Dtype: float64

Điểm tổng kết (top 3):
  1. Sinh viên 10: 9.20 (Loại A)
  2. Sinh viên 3:  8.70 (Loại A)
  3. Sinh viên 7:  8.65 (Loại A)

Xếp loại:
  - Loại A (≥8.5): 3 sinh viên
  - Loại B (7.0-8.4): 3 sinh viên
  - Loại C (5.5-6.9): 3 sinh viên
  - Loại D (4.0-5.4): 1 sinh viên

Sinh viên cần hỗ trợ:
  - Sinh viên 6: 5.10 điểm (chuyên cần 4.5 < 5.0)

Z-score analysis (điểm cuối kỳ):
  - Trung bình: 7.25
  - Độ lệch chuẩn: 1.33
  - Phạm vi: 5.0 - 9.0
```

### Kỹ thuật chính
- Matrix multiplication: `scores @ weights`
- Boolean indexing: `scores < 5.0`
- Z-score normalization: `(x - mean) / std`

---

## 📚 BÀI 2: PHÂN TÍCH CHUYÊN CẦN

### Input
- 12 sinh viên, 8 buổi học
- Quy ước: 1 = có mặt, 0 = vắng

### Output Chính
```
Chuyên cần tổng quan:
  - Tỉ lệ trung bình: 76.0%
  - Sinh viên đầy đủ: 1 (8%)
  - Sinh viên cảnh báo (<75%): 5 (42%)

Sinh viên bị cảnh báo:
  - SV3: 62.5% (5/8 buổi)
  - SV5: 62.5% (5/8 buổi)
  - SV7: 50.0% (4/8 buổi) ← Nghiêm trọng nhất
  - SV9: 62.5% (5/8 buổi)
  - SV11: 62.5% (5/8 buổi)

Buổi có vắng nhiều nhất:
  - Buổi 4 & 6: 4 sinh viên vắng
```

### Nhận xét
- ⚠ Ý thức học tập cần cải thiện
- Cần tư vấn 5 sinh viên về tầm quan trọng chuyên cần

### Kỹ thuật chính
- np.where(): Tìm sinh viên thỏa điều kiện
- np.any(): Kiểm tra 2 buổi vắng liên tiếp

---

## 💰 BÀI 3: PHÂN TÍCH DOANH THU

### Input
- 5 sản phẩm, 7 ngày
- Doanh thu tính bằng triệu đồng

### Output Chính
```
Tổng doanh thu tuần: 5,224 triệu đồng

Doanh thu theo sản phẩm:
  1. SP5: 1,162 triệu đồng ⭐ (Doanh số tốt nhất)
  2. SP2: 1,107 triệu đồng
  3. SP4: 1,052 triệu đồng
  4. SP3: 970 triệu đồng
  5. SP1: 933 triệu đồng

Ngày tốt nhất:
  - Ngày 7: 800 triệu đồng (cao nhất)
  - Trung bình: 746.29 triệu đồng/ngày

Độ ổn định (độ lệch chuẩn):
  1. SP5: 5.68 ← Ổn định nhất ✓
  2. SP4: 6.56
  3. SP3: 7.40
  4. SP2: 8.06
  5. SP1: 8.14

Kịch bản tăng 8% cho SP2 & SP5:
  - Tổng trước: 5,224 triệu đồng
  - Tổng sau: 5,405 triệu đồng
  - Mức tăng: +181 triệu đồng (3.47%)
```

### Khuyến nghị
✓ Ưu tiên bán SP5 (cao nhất + ổn định)
✓ Tăng quảng cáo SP1 (doanh thu thấp)

### Kỹ thuật chính
- np.std(): Tìm sản phẩm ổn định
- Boolean indexing: Lọc ngày trên trung bình

---

## 📦 BÀI 4: QUẢN LÝ TỒN KHO

### Input
- 10 mặt hàng
- Tồn kho hiện tại, mức tối thiểu, giá nhập

### Output Chính
```
Trạng thái kho:
  - Mặt hàng đủ: 4 (HH1, HH5, HH8, HH10)
  - Mặt hàng thiếu: 6 (HH2, HH3, HH4, HH6, HH7, HH9)
  - Tổng thiếu hụt: 25 đơn vị (15.4%)

Top 3 mặt hàng thiếu nhiều nhất:
  1. HH2: Thiếu 7 đơn vị (8 → 15) 💰 175 triệu đ
  2. HH7: Thiếu 5 đơn vị (7 → 12) 💰 90 triệu đ
  3. HH4: Thiếu 5 đơn vị (5 → 10) 💰 110 triệu đ

Chi phí nhập hàng:
  - Tổng chi phí: 556 triệu đồng
  - Không có nhập hàng phải giới hạn (tất cả ≤ 20)
  - Tiết kiệm: 0 triệu đồng
```

### Mức độ thiếu hụt
- Trung bình: Cần ưu tiên nhập
- Không quá nghiêm trọng nhưng cần xử lý nhanh

### Kỹ thuật chính
- np.maximum(): Tính lượng cần nhập
- np.clip(): Giới hạn tối đa 20 đơn vị

---

## 🔍 BÀI 5: TỔNG HỢP VÀ SO SÁNH

### Câu 1: Giống nhau về cấu trúc?
✓ **Cả hai đều là ma trận 2D**
  - Bài 1: 10 sinh viên × 4 thành phần
  - Bài 3: 7 ngày × 5 sản phẩm

✓ **Theo dõi nhiều đối tượng qua nhiều tiêu chí**
  - Bài 1: Sinh viên qua 4 thành phần điểm
  - Bài 3: Sản phẩm qua 7 ngày

✓ **Dùng dtype float/numeric**
✓ **Tính toán chỉ số tổng hợp (weighting/summing)**

### Câu 2: Phép toán NumPy nào được dùng ở cả hai?
| Phép toán | Bài 1 | Bài 3 | Mô tả |
|-----------|-------|-------|-------|
| .sum() | ✓ | ✓ | Cộng phần tử |
| .mean() | ✓ | ✓ | Trung bình |
| .std() | ✓ | ✓ | Độ lệch chuẩn |
| .max(), .min() | ✓ | ✓ | Cực trị |
| np.where() | ✓ | ✓ | Lọc dữ liệu |
| @ (matrix mult) | ✓ | | Tính weighted sum |

### Câu 3: Bài nào dùng boolean indexing nhiều hơn?
**→ Bài 1 dùng nhiều hơn** 🏆

VÌ SAO?
- Bài 1 (Giáo dục): Phân loại, xếp hạng, cảnh báo → nhiều điều kiện
- Bài 3 (Kinh doanh): Chủ yếu aggregation (tổng, trung bình) → ít điều kiện

Ví dụ:
```python
# Bài 1: Nhiều boolean indexing
grades = np.array([classify_grade(s) for s in scores])  # Phân loại
low_scores = scores < 5.0  # Phát hiện điểm thấp
good_students = np.where(final_score >= 7.0)[0]  # Lọc tốt

# Bài 3: Ít boolean indexing
high_days = np.where(daily_total > daily_total.mean())[0]  # Chỉ 1 lần
```

### Câu 4: Lợi ích của vectorization so với vòng lặp?

**Bằng chứng thực tế (1000 lần chạy):**
```
Vectorized (@):  2.73 ms
Loop approach:  72.94 ms
╔═══════════════════════════════════════╗
║ Tăng tốc: 26.7x lần nhanh hơn!      ║
╚═══════════════════════════════════════╝
```

**5 lợi ích chính:**
1. **Hiệu suất:** 10-100x nhanh hơn
2. **Code ngắn gọn:** 1 dòng vs 10 dòng
3. **Bộ nhớ:** Arrays lưu trữ liên tiếp, cache-friendly
4. **Tránh lỗi:** Không cần lo off-by-one errors
5. **Linh hoạt:** Hoạt động với tensor bất kỳ

### Câu 5: Khi tăng 100 lần, NumPy hỗ trợ gì?

**8 Cơ chế scalability:**

1. **Advanced Indexing** → Xử lý 1M phần tử nhanh
2. **Cache-friendly operations** → Tối ưu CPU
3. **Memory Mapping** → Xử lý file > RAM
4. **Broadcasting** → Tiết kiệm bộ nhớ
5. **DTYPE optimization** → float32 vs float64
6. **Parallel Processing** → Numba, GPU (CuPy), Dask
7. **Chunking** → Chia dữ liệu lớn thành chunks
8. **Efficient Sorting** → O(n log n) complexity

**Ví dụ:** 1M sinh viên × 100 thuộc tính → **1-2 giây** ⚡

---

## 📈 SO SÁNH TỔNG HỢP

```
+========================+=====================+=====================+
| Tiêu chí               | Bài 1 (Giáo dục)    | Bài 3 (Kinh doanh)   |
+========================+=====================+=====================+
| Shape                  | (10, 4)             | (7, 5)              |
| Axis 0 (Hàng)          | Sinh viên           | Ngày                |
| Axis 1 (Cột)           | 4 thành phần        | 5 sản phẩm          |
| Phép aggregation       | matrix mult         | sum axis            |
| Boolean indexing       | NHIEU (phân loại)   | IT (aggregation)    |
| Tính phân hóa          | Cao (std, z-score)  | Vừa phải (std)      |
| Mục tiêu               | Quản lý/Cảnh báo    | Xu hướng/Quy hoạch  |
+========================+=====================+=====================+
```

---

## ✨ KẾT LUẬN

1. **NumPy tối ưu** cho phân tích dữ liệu 2D - cung cấp các công cụ mạnh mẽ cho tính toán ma trận
2. **Vectorization** giúp tăng tốc 26x-100x lần so với vòng lặp truyền thống
3. **Boolean indexing** là kỹ năng then chốt trong Bài 1 - dùng cho phân loại, xếp hạng, cảnh báo
4. **Các phép toán chung** (sum, mean, std, where) được dùng ở cả 2 miền - chứng tỏ tính phổ quát
5. **Khi dữ liệu tăng 100x**, NumPy vẫn xử lý hiệu quả nhờ tối ưu hóa C-level

### So Sánh Miền Giáo dục vs Kinh doanh
| Tiêu chí | Bài 1 (Điểm) | Bài 3 (Doanh thu) |
|----------|-------------|-----------------|
| Cấu trúc ma trận | 10×4 | 7×5 |
| Mục tiêu chính | Phân loại, cảnh báo | Xu hướng, quy hoạch |
| Boolean indexing | NHIỀU | ÍT |
| Phép toán chủ yếu | Matrix mult, Z-score | Sum, Mean, Std |
| Ứng dụng thực tiễn | Quản lý học viên | Quy hoạch bán hàng |

---

## 🚀 HƯỚNG PHÁT TRIỂN

- [ ] Thêm visualization (matplotlib, seaborn)
- [ ] Sử dụng pandas DataFrame cho dữ liệu lớn hơn
- [ ] Áp dụng machine learning (scikit-learn)
- [ ] Triển khai real-time analytics
- [ ] Tối ưu hóa với GPU (CuPy)
- [ ] Tạo dashboard tương tác với Streamlit
- [ ] Xuất báo cáo tự động (PDF, Excel)

---

## 📚 THAM KHẢO

### Các hàm NumPy quan trọng được dùng
- **Aggregation**: sum(), mean(), std(), max(), min()
- **Indexing**: where(), argmax(), argmin()
- **Broadcasting**: Phép toán tự động giữa mảng khác kích thước
- **Matrix operations**: @ (matrix multiplication), dot()
- **Statistical**: mean(), std(), percentile()
- **Utilities**: any(), all(), clip(), round()

### Độ phức tạp thời gian
- Sum/Mean/Std: O(n) - tuyến tính
- Sorting: O(n log n)
- Matrix multiplication: O(n³) - có thể tối ưu với BLAS
- Where/Indexing: O(n) - tuyến tính

---



