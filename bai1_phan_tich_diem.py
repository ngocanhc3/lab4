"""
Bài 1 - Phân tích điểm học phần theo miền Giáo dục
Phân tích điểm của 10 sinh viên với 4 thành phần: chuyên cần, giữa kỳ, thực hành, cuối kỳ
"""

import numpy as np

# ============== 1. Tạo ma trận điểm ==============
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

print("="*70)
print("BÀI 1: PHÂN TÍCH ĐIỂM HỌC PHẦN THEO MIỀN GIÁO DỤC")
print("="*70)

print("\n1. THÔNG TIN CẤU TRÚC MA TRẬN ĐIỂM")
print("-" * 70)
print(f"Shape (hình dạng): {scores.shape}")
print(f"  - Số sinh viên: {scores.shape[0]}")
print(f"  - Số thành phần điểm: {scores.shape[1]}")
print(f"Ndim (số chiều): {scores.ndim}")
print(f"Dtype (kiểu dữ liệu): {scores.dtype}")

print("\nMa trận điểm:\n", scores)

# ============== 2. Tính điểm tổng kết theo trọng số ==============
print("\n2. TÍNH ĐIỂM TỔNG KẾT THEO TRỌNG SỐ")
print("-" * 70)
weights = np.array([0.1, 0.2, 0.3, 0.4])  # chuyên cần, giữa kỳ, thực hành, cuối kỳ
final_score = scores @ weights  # Phép nhân ma trận

print(f"Trọng số: Chuyên cần={weights[0]*100}%, Giữa kỳ={weights[1]*100}%, Thực hành={weights[2]*100}%, Cuối kỳ={weights[3]*100}%")
print("\nĐiểm tổng kết của từng sinh viên:")
for i, score in enumerate(final_score):
    print(f"  Sinh viên {i+1}: {score:.2f}")

# ============== 3. Xếp loại sinh viên ==============
print("\n3. XẾP LOẠI SINH VIÊN THEO THANG A, B, C, D")
print("-" * 70)

def classify_grade(score):
    if score >= 8.5:
        return 'A'
    elif score >= 7.0:
        return 'B'
    elif score >= 5.5:
        return 'C'
    elif score >= 4.0:
        return 'D'
    else:
        return 'F'

grades = np.array([classify_grade(score) for score in final_score])

print("Xếp loại:")
for i, (score, grade) in enumerate(zip(final_score, grades)):
    print(f"  Sinh viên {i+1}: {score:.2f} → Loại {grade}")

grade_counts = {grade: np.sum(grades == grade) for grade in ['A', 'B', 'C', 'D', 'F']}
print("\nThống kê xếp loại:")
for grade, count in grade_counts.items():
    if count > 0:
        print(f"  Loại {grade}: {count} sinh viên")

# ============== 4. Tìm sinh viên cao nhất và thấp nhất ==============
print("\n4. SINH VIÊN CÓ ĐIỂM CAO NHẤT VÀ THẤP NHẤT")
print("-" * 70)
max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)

print(f"Sinh viên cao nhất: Sinh viên {max_idx+1} với điểm {final_score[max_idx]:.2f}")
print(f"  Chi tiết: Chuyên cần={scores[max_idx][0]}, Giữa kỳ={scores[max_idx][1]}, Thực hành={scores[max_idx][2]}, Cuối kỳ={scores[max_idx][3]}")
print(f"\nSinh viên thấp nhất: Sinh viên {min_idx+1} với điểm {final_score[min_idx]:.2f}")
print(f"  Chi tiết: Chuyên cần={scores[min_idx][0]}, Giữa kỳ={scores[min_idx][1]}, Thực hành={scores[min_idx][2]}, Cuối kỳ={scores[min_idx][3]}")

# ============== 5. Lọc sinh viên có điểm từ 7.0 trở lên ==============
print("\n5. LỌC SINH VIÊN CÓ ĐIỂM TỪ 7.0 TRỞ LÊN")
print("-" * 70)
good_students = np.where(final_score >= 7.0)[0]

print(f"Số sinh viên: {len(good_students)}")
print("Danh sách:")
for idx in good_students:
    print(f"  Sinh viên {idx+1}: {final_score[idx]:.2f}")

# ============== 6. Phát hiện sinh viên có thành phần điểm dưới 5.0 ==============
print("\n6. SINH VIÊN CÓ ÍT NHẤT MỘT THÀNH PHẦN ĐIỂM DƯỚI 5.0")
print("-" * 70)
low_component = np.any(scores < 5.0, axis=1)
low_students = np.where(low_component)[0]

print(f"Số sinh viên: {len(low_students)}")
print("Danh sách:")
for idx in low_students:
    low_cols = np.where(scores[idx] < 5.0)[0]
    col_names = ['Chuyên cần', 'Giữa kỳ', 'Thực hành', 'Cuối kỳ']
    print(f"  Sinh viên {idx+1}:")
    for col_idx in low_cols:
        print(f"    - {col_names[col_idx]}: {scores[idx, col_idx]}")

# ============== 7. Sắp xếp và tìm 3 sinh viên đứng đầu ==============
print("\n7. 3 SINH VIÊN ĐỨng ĐẦU THEO ĐIỂM TỔNG KẾT")
print("-" * 70)
rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3]

print("Top 3 sinh viên:")
for rank, idx in enumerate(top3, 1):
    print(f"  {rank}. Sinh viên {idx+1}: {final_score[idx]:.2f} ({grades[idx]})")

# ============== 8. Chuẩn hóa điểm cuối kỳ theo Z-score ==============
print("\n8. CHUẨN HÓA ĐIỂM CUỐI KỲ THEO Z-SCORE")
print("-" * 70)
final_exam_scores = scores[:, 3]
z_scores = (final_exam_scores - final_exam_scores.mean()) / final_exam_scores.std()

mean_final = final_exam_scores.mean()
std_final = final_exam_scores.std()

print(f"Thống kê điểm cuối kỳ:")
print(f"  - Trung bình: {mean_final:.2f}")
print(f"  - Độ lệch chuẩn: {std_final:.2f}")
print(f"  - Giá trị tối thiểu: {final_exam_scores.min():.2f}")
print(f"  - Giá trị tối đa: {final_exam_scores.max():.2f}")
print(f"  - Phạm vi (Range): {final_exam_scores.max() - final_exam_scores.min():.2f}")

print("\nZ-score của từng sinh viên:")
for i, (score, z_score) in enumerate(zip(final_exam_scores, z_scores)):
    print(f"  Sinh viên {i+1}: Điểm={score:.2f}, Z-score={z_score:.3f}")

print("\nNHẬN XÉT VỀ MỨC ĐỘ PHÂN HÓA:")
print("-" * 70)
high_z_count = np.sum(z_scores > 1)
low_z_count = np.sum(z_scores < -1)
print(f"• Độ lệch chuẩn {std_final:.2f} cho thấy mức độ phân hóa TRUNG BÌNH")
print(f"• Có {high_z_count} sinh viên có điểm cao bất thường (Z > 1)")
print(f"• Có {low_z_count} sinh viên có điểm thấp bất thường (Z < -1)")
print(f"• Điểm cuối kỳ phân bố khá rộng từ {final_exam_scores.min():.1f} đến {final_exam_scores.max():.1f}")
print(f"• Điều này cho thấy sự khác biệt rõ rệt trong năng lực của các sinh viên")

print("\n" + "="*70)
print("KẾT LUẬN")
print("="*70)
print(f"• Tổng {len(good_students)}/{len(final_score)} sinh viên đạt trên 7.0 điểm")
print(f"• Có {len(low_students)} sinh viên có thành phần điểm dưới 5.0 cần hỗ trợ")
print(f"• Sinh viên {max_idx+1} là học sinh xuất sắc với điểm {final_score[max_idx]:.2f}")
print(f"• Sinh viên {min_idx+1} cần được theo dõi đặc biệt với điểm {final_score[min_idx]:.2f}")

