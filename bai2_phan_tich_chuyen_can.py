"""
Bài 2 - Phân tích chuyên cần và cảnh báo học vụ
Theo dõi chuyên cần của 12 sinh viên trong 8 buổi học (1=có mặt, 0=vắng)
"""

import numpy as np

print("="*70)
print("BÀI 2: PHÂN TÍCH CHUYÊN CẦN VÀ CẢNH BÁO HỌC VỤ")
print("="*70)

# ============== 1. Tạo ma trận chuyên cần ==============
attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

print("\n1. MA TRẬN CHUYÊN CẦN VÀ TỔNG SỐ BUỔI ĐI HỌC")
print("-" * 70)
print("Ma trận chuyên cần (1=có mặt, 0=vắng):\n", attendance)

present_count = attendance.sum(axis=1)

print(f"\nTổng số buổi đi học của từng sinh viên:")
for i, count in enumerate(present_count):
    print(f"  Sinh viên {i+1}: {int(count)}/8 buổi")

# ============== 2. Tính tỉ lệ chuyên cần ==============
print("\n2. TỈ LỆ CHUYÊN CẦN THEO PHẦN TRĂM")
print("-" * 70)
rate = present_count / attendance.shape[1] * 100

print(f"Tỉ lệ chuyên cần của từng sinh viên:")
for i, (count, r) in enumerate(zip(present_count, rate)):
    print(f"  Sinh viên {i+1}: {int(count)}/8 buổi = {r:.1f}%")

# ============== 3. Xác định sinh viên bị cảnh báo ==============
print("\n3. SINH VIÊN BỊ CẢNH BÁO (TỈ LỆ < 75%)")
print("-" * 70)
warning_idx = np.where(rate < 75)[0]

if len(warning_idx) > 0:
    print(f"Số sinh viên bị cảnh báo: {len(warning_idx)}")
    for idx in warning_idx:
        print(f"  Sinh viên {idx+1}: {rate[idx]:.1f}% ({int(present_count[idx])}/8 buổi)")
else:
    print("Không có sinh viên nào bị cảnh báo!")

# ============== 4. Tìm buổi học có số lượng vắng nhiều nhất ==============
print("\n4. BUỔI HỌC CÓ SỐ LƯỢNG VẮNG NHIỀU NHẤT")
print("-" * 70)
absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session)

print(f"\nSố lượng vắng ở từng buổi:")
for session, absent_count in enumerate(absent_count_by_session):
    status = " <-- Nhiều vắng nhất" if session == worst_session else ""
    print(f"  Buổi {session+1}: {int(absent_count)} sinh viên vắng{status}")

print(f"\nBuổi học có nhiều vắng nhất: Buổi {worst_session+1} với {int(absent_count_by_session[worst_session])} sinh viên vắng")

# ============== 5. Tìm sinh viên đi học đầy đủ ==============
print("\n5. SINH VIÊN ĐI HỌC ĐẦY ĐỦ CẢ 8 BUỔI")
print("-" * 70)
full_attendance_mask = np.all(attendance == 1, axis=1)
full_attendance = np.where(full_attendance_mask)[0]

if len(full_attendance) > 0:
    print(f"Số sinh viên đi học đầy đủ: {len(full_attendance)}")
    for idx in full_attendance:
        print(f"  Sinh viên {idx+1}")
else:
    print("Không có sinh viên nào đi học đầy đủ!")

# ============== 6. Phát hiện sinh viên có từ 2 buổi vắng liên tiếp ==============
print("\n6. SINH VIÊN CÓ TỪ 2 BUỔI VẮNG LIÊN TIẾP TRỞ LÊN")
print("-" * 70)

# Tìm 2 buổi vắng liên tiếp
two_absent_in_row = np.where(np.any((attendance[:, :-1] == 0) & (attendance[:, 1:] == 0), axis=1))[0]

if len(two_absent_in_row) > 0:
    print(f"Số sinh viên vắng 2 buổi liên tiếp trở lên: {len(two_absent_in_row)}")
    for idx in two_absent_in_row:
        # Tìm vị trí vắng liên tiếp
        row = attendance[idx]
        consecutive_absent = []
        i = 0
        while i < len(row) - 1:
            if row[i] == 0 and row[i+1] == 0:
                start = i
                while i < len(row) and row[i] == 0:
                    i += 1
                consecutive_absent.append((start+1, i))  # +1 để match buổi thực tế
            else:
                i += 1
        
        print(f"  Sinh viên {idx+1}:")
        for start, end in consecutive_absent:
            print(f"    - Vắng từ buổi {start} đến buổi {end-1} ({end-start} buổi liên tiếp)")
else:
    print("Không có sinh viên nào vắng 2 buổi liên tiếp!")

# ============== 7. Nhận xét ngắn ==============
print("\n7. NHẬN XÉT VỀ Ý THỨC HỌC TẬP CỦA LỚP")
print("-" * 70)

total_absent = (attendance == 0).sum()
avg_rate = rate.mean()
excellent_count = np.sum(rate >= 100)
good_count = np.sum((rate >= 87.5) & (rate < 100))
warning_count = len(warning_idx)

print(f"\nStatistics:")
print(f"• Tổng số buổi vắng toàn lớp: {total_absent}")
print(f"• Tỉ lệ chuyên cần trung bình: {avg_rate:.1f}%")
print(f"• Sinh viên đi đầy đủ: {excellent_count} ({excellent_count/len(attendance)*100:.0f}%)")
print(f"• Sinh viên chỉnh chu (≥87.5%): {good_count} ({good_count/len(attendance)*100:.0f}%)")
print(f"• Sinh viên cần cảnh báo (<75%): {warning_count} ({warning_count/len(attendance)*100:.0f}%)")

print(f"\nNhận xét:")
if avg_rate >= 90:
    print("✓ Ý thức học tập của lớp rất tốt - phần lớn sinh viên đi học đầy đủ")
elif avg_rate >= 80:
    print("⚠ Ý thức học tập của lớp khá tốt - tuy nhiên còn một số sinh viên cần chú ý")
else:
    print("✗ Ý thức học tập của lớp cần cải thiện - có nhiều sinh viên vắng học")

if warning_count > 0:
    print(f"• Cần tập trung hỗ trợ {warning_count} sinh viên bị cảnh báo")

if len(two_absent_in_row) > 0:
    print(f"• {len(two_absent_in_row)} sinh viên có dấu hiệu vắng học liên tiếp - cảnh báo sớm cần thiết")

print("\n" + "="*70)
print("KẾT LUẬN")
print("="*70)
if warning_count == 0:
    print("✓ Toàn bộ sinh viên đều đạt tỉ lệ chuyên cần yêu cầu (≥75%)")
else:
    print(f"⚠ {warning_count} sinh viên cần được tư vấn về tầm quan trọng của chuyên cần")

