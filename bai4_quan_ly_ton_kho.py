"""
Bài 4 - Quản lý tồn kho và đề xuất nhập hàng
Quản lý 10 mặt hàng với dữ liệu tồn kho, mức tối thiểu và giá nhập
"""

import numpy as np

print("="*70)
print("BÀI 4: QUẢN LÝ TỒN KHO VÀ ĐỀ XUẤT NHẬP HÀNG")
print("="*70)

# ============== Dữ liệu ==============
stock = np.array([35, 8, 12, 5, 40, 18, 7, 22, 9, 15])
min_stock = np.array([20, 15, 15, 10, 25, 20, 12, 18, 12, 15])
price = np.array([30, 25, 28, 22, 35, 20, 18, 24, 19, 21])

product_names = [f"Hàng hóa {i+1}" for i in range(len(stock))]

print("\nDỮ LIỆU KHOẢNG HÀng:\n")
print(f"{'Hàng hóa':<12} {'Tồn kho':<10} {'Mức tối thiểu':<15} {'Giá nhập':<10}")
print("-" * 50)
for i, name in enumerate(product_names):
    print(f"{name:<12} {stock[i]:<10} {min_stock[i]:<15} {price[i]:<10}")

# ============== 1. Xác định mặt hàng đang thiếu ==============
print("\n1. MẶT HÀNG ĐANG THIẾU SO VỚI MỨC TỐI THIỂU")
print("-" * 70)
shortage_mask = stock < min_stock
shortage_items = np.where(shortage_mask)[0]

print(f"Số mặt hàng thiếu: {len(shortage_items)}/10")
print(f"\nMặt hàng thiếu:")
for idx in shortage_items:
    shortage = min_stock[idx] - stock[idx]
    print(f"  {product_names[idx]}: Tồn={stock[idx]}, Thiếu {int(shortage)} (từ {stock[idx]} lên {min_stock[idx]})")

# ============== 2. Tính số lượng cần nhập ==============
print("\n2. SỐ LƯỢNG CẦN NHẬP CHO TỪNG MẶT HÀNG")
print("-" * 70)
need_import = np.maximum(min_stock - stock, 0)

print(f"{'Hàng hóa':<12} {'Tồn kho':<10} {'Cần nhập':<15} {'Ghi chú':<20}")
print("-" * 57)
for i, name in enumerate(product_names):
    if need_import[i] > 0:
        print(f"{name:<12} {stock[i]:<10} {int(need_import[i]):<15} Thiếu hàng")
    else:
        print(f"{name:<12} {stock[i]:<10} {int(need_import[i]):<15} Đủ hàng")

# ============== 3. Tính chi phí nhập chỉ cho mặt hàng thiếu ==============
print("\n3. CHI PHÍ NHẬP THÊM CHO CÁC MẶT HÀNG THIẾU")
print("-" * 70)
cost = need_import * price

print(f"{'Hàng hóa':<12} {'Cần nhập':<10} {'Giá/đơn vị':<15} {'Tổng chi phí':<15}")
print("-" * 52)
for i, name in enumerate(product_names):
    if need_import[i] > 0:
        print(f"{name:<12} {int(need_import[i]):<10} {price[i]:<15} {int(cost[i])} (triệu đ)")

# ============== 4. Tính tổng chi phí nhập hàng ==============
print("\n4. TỔNG CHI PHÍ NHẬP HÀNG")
print("-" * 70)
total_cost = cost.sum()
print(f"Tổng chi phí nhập hàng: {int(total_cost)} triệu đồng")

print(f"\nChi tiết:")
print(f"  - Chi phí cho mặt hàng thiếu: {int(cost[shortage_mask].sum())} triệu đồng")
print(f"  - Chi phí cho mặt hàng đủ: {int(cost[~shortage_mask].sum())} triệu đồng")

# ============== 5. Phân loại trạng thái từng mặt hàng ==============
print("\n5. PHÂN LOẠI TRẠNG THÁI MỖI MẶT HÀNG")
print("-" * 70)
status = np.where(stock < min_stock, "Thiếu hàng", "Đủ hàng")

print(f"{'Hàng hóa':<12} {'Tồn kho':<10} {'Mức tối thiểu':<15} {'Trạng thái':<15}")
print("-" * 52)
for i, name in enumerate(product_names):
    status_icon = "✗" if status[i] == "Thiếu hàng" else "✓"
    print(f"{name:<12} {stock[i]:<10} {min_stock[i]:<15} {status_icon} {status[i]:<15}")

# ============== 6. Tìm 3 mặt hàng thiếu nhiều nhất ==============
print("\n6. 3 MẶT HÀNG THIẾU NHIỀU NHẤT")
print("-" * 70)
top3_shortage = np.argsort(need_import)[::-1][:3]

print("Top 3 mặt hàng cần nhập khẩn cấp nhất:")
for rank, idx in enumerate(top3_shortage, 1):
    if need_import[idx] > 0:
        print(f"  {rank}. {product_names[idx]}: Cần nhập {int(need_import[idx])} đơn vị (Chi phí: {int(cost[idx])} triệu đ)")
    else:
        print(f"  {rank}. {product_names[idx]}: Không cần nhập")

# ============== 7. Giới hạn lượng nhập tối đa ==============
print("\n7. GIỚI HẠN LƯỢNG NHẬP TỐI ĐA 20 ĐƠN VỊ (np.clip)")
print("-" * 70)
limited_need = np.clip(need_import, 0, 20)

print(f"{'Hàng hóa':<12} {'Cần nhập':<15} {'Nhập tối đa':<15} {'Giới hạn?':<12}")
print("-" * 54)
for i, name in enumerate(product_names):
    limited = "Có" if limited_need[i] < need_import[i] else "Không"
    if need_import[i] > 0:
        print(f"{name:<12} {int(need_import[i]):<15} {int(limited_need[i]):<15} {limited:<12}")

# ============== 8. Tính lại tổng chi phí sau giới hạn ==============
print("\n8. CHI PHÍ NHẬP HÀNG SAU KHI GIỚI HẠN TỐI ĐA 20 ĐƠN VỊ")
print("-" * 70)
limited_cost = limited_need * price
limited_total_cost = limited_cost.sum()

print(f"{'Hàng hóa':<12} {'Nhập tối đa':<12} {'Giá/đơn vị':<12} {'Chi phí':<12}")
print("-" * 48)
for i, name in enumerate(product_names):
    if limited_need[i] > 0:
        print(f"{name:<12} {int(limited_need[i]):<12} {price[i]:<12} {int(limited_cost[i]):<12}")

print(f"\nTổng chi phí sau giới hạn: {int(limited_total_cost)} triệu đồng")
print(f"Chi phí trước giới hạn:    {int(total_cost)} triệu đồng")
print(f"Tiết kiệm:                {int(total_cost - limited_total_cost)} triệu đồng")

# ============== 9. Nhận xét ==============
print("\n9. NHẬN XÉT VỀ MỨC ĐỘ THIẾU HỤT CỦA KHO")
print("-" * 70)

total_shortage = need_import.sum()
total_stock_capacity = min_stock.sum()
shortage_percent = (total_shortage / total_stock_capacity) * 100

print(f"\nThống kê tổng quan:")
print(f"  - Tổng tồn kho hiện tại: {stock.sum()}")
print(f"  - Tổng mức tối thiểu: {min_stock.sum()}")
print(f"  - Tổng thiếu hụt: {int(total_shortage)}")
print(f"  - Tỉ lệ thiếu hụt: {shortage_percent:.1f}%")

print(f"\nPhân tích:")
if len(shortage_items) == 0:
    print("  ✓ Kho có đủ hàng cho tất cả mặt hàng")
elif len(shortage_items) <= 2:
    print("  ⚠ Chỉ có ít mặt hàng thiếu - tình hình chưa quá nghiêm trọng")
else:
    print(f"  ✗ Có {len(shortage_items)} mặt hàng thiếu - cần nhập hàng khẩn cấp")

if shortage_percent < 10:
    print("  → Mức độ thiếu hụt nhẹ - có thể xử lý từ từ")
elif shortage_percent < 30:
    print("  → Mức độ thiếu hụt trung bình - cần ưu tiên")
else:
    print("  → Mức độ thiếu hụt cao - cần xử lý ngay lập tức")

# Phân loại mặt hàng cần ưu tiên
critical_items = np.where((stock < min_stock) & (need_import > 10))[0]
urgent_items = np.where((stock < min_stock) & (need_import <= 10))[0]

if len(critical_items) > 0:
    print(f"\n  Mặt hàng cần nhập khẩn cấp ({len(critical_items)}):")
    for idx in critical_items:
        print(f"    • {product_names[idx]}: Thiếu {int(need_import[idx])} đơn vị")

if len(urgent_items) > 0:
    print(f"\n  Mặt hàng cần nhập ưu tiên ({len(urgent_items)}):")
    for idx in urgent_items:
        print(f"    • {product_names[idx]}: Thiếu {int(need_import[idx])} đơn vị")

print("\n" + "="*70)
print("KHUYẾN NGHỊ")
print("="*70)
print(f"1. Nhập hàng ngay {len(critical_items)} mặt hàng cấp tính")
print(f"2. Lên kế hoạch nhập {len(urgent_items)} mặt hàng khác trong thời gian sớm")
print(f"3. Chi phí dự kiến: {int(limited_total_cost)} triệu đồng (với giới hạn 20 đơn vị/mặt hàng)")
print(f"4. Tối ưu hóa: Nếu nhập đầy đủ sẽ cần {int(total_cost)} triệu đồng")

