"""
Bài 3 - Phân tích doanh thu bán hàng theo miền Kinh doanh
Phân tích doanh thu của 5 sản phẩm trong 7 ngày
"""

import numpy as np

print("="*70)
print("BÀI 3: PHÂN TÍCH DOANH THU BÁN HÀNG THEO MIỀN KINH DOANH")
print("="*70)

# ============== 1. Tạo ma trận doanh thu ==============
sales = np.array([
    [120, 150, 130, 140, 160],  # Ngày 1: 5 sản phẩm
    [125, 145, 128, 142, 158],  # Ngày 2
    [130, 155, 135, 150, 162],  # Ngày 3
    [135, 160, 140, 152, 168],  # Ngày 4
    [140, 165, 145, 155, 170],  # Ngày 5
    [138, 162, 142, 153, 169],  # Ngày 6
    [145, 170, 150, 160, 175]   # Ngày 7
])

print("\n1. MA TRẬN DOANH THU VÀ TỔNG THEO NGÀY")
print("-" * 70)
print("Doanh thu 7 ngày của 5 sản phẩm (đơn vị: triệu đồng):")
print("        SP1   SP2   SP3   SP4   SP5")
for day, row in enumerate(sales):
    print(f"Ngày {day+1}: {row}")

daily_total = sales.sum(axis=1)

print(f"\nTổng doanh thu theo từng ngày:")
for day, total in enumerate(daily_total):
    print(f"  Ngày {day+1}: {int(total)} triệu đồng")

# ============== 2. Tổng doanh thu và trung bình theo sản phẩm ==============
print("\n2. TỔNG DOANH THU VÀ DOANH THU TRUNG BÌNH THEO SẢN PHẨM")
print("-" * 70)
product_total = sales.sum(axis=0)
product_mean = sales.mean(axis=0)
product_names = ['Sản phẩm 1', 'Sản phẩm 2', 'Sản phẩm 3', 'Sản phẩm 4', 'Sản phẩm 5']

print(f"{'Sản phẩm':<15} {'Tổng doanh thu':<20} {'Trung bình/ngày':<20}")
print("-" * 55)
for i, name in enumerate(product_names):
    print(f"{name:<15} {int(product_total[i]):<20} {product_mean[i]:<20.2f}")

# ============== 3. Ngày cao nhất và sản phẩm bán tốt nhất ==============
print("\n3. NGÀY CÓ DOANH THU CAO NHẤT VÀ SẢN PHẨM BÁN TỐT NHẤT TOÀN TUẦN")
print("-" * 70)
best_day = np.argmax(daily_total)
best_product = np.argmax(product_total)

print(f"Ngày có doanh thu cao nhất: Ngày {best_day+1}")
print(f"  - Tổng doanh thu: {int(daily_total[best_day])} triệu đồng")
print(f"  - Chi tiết từng sản phẩm: {sales[best_day]}")

print(f"\nSản phẩm bán tốt nhất toàn tuần: Sản phẩm {best_product+1}")
print(f"  - Tổng doanh thu: {int(product_total[best_product])} triệu đồng")
print(f"  - Doanh thu trung bình: {product_mean[best_product]:.2f} triệu đồng/ngày")
print(f"  - Doanh thu theo ngày: {sales[:, best_product]}")

# ============== 4. Tăng doanh số sản phẩm 2 và 5 thêm 8% ==============
print("\n4. TẠO MA TRẬN DOANH THU MỚI SAU KHI TĂNG SP2 VÀ SP5 THÊM 8%")
print("-" * 70)
new_sales = sales.astype(float).copy()
new_sales[:, [1, 4]] *= 1.08  # SP2 (index 1) và SP5 (index 4)

print("Ma trận doanh thu sau điều chỉnh:")
print("        SP1    SP2    SP3    SP4    SP5")
for day, row in enumerate(new_sales):
    print(f"Ngày {day+1}: {row}")

# ============== 5. So sánh tổng doanh thu trước và sau ==============
print("\n5. SO SÁNH TỔNG DOANH THU TOÀN TUẦN TRƯỚC VÀ SAU ĐIỀU CHỈNH")
print("-" * 70)
before_total = sales.sum()
after_total = new_sales.sum()
increase = after_total - before_total
increase_percent = (increase / before_total) * 100

print(f"Tổng doanh thu trước điều chỉnh: {int(before_total)} triệu đồng")
print(f"Tổng doanh thu sau điều chỉnh:  {int(after_total)} triệu đồng")
print(f"Mức tăng: {int(increase)} triệu đồng ({increase_percent:.2f}%)")

print(f"\nBefore và After từng sản phẩm:")
for i, name in enumerate(product_names):
    before = product_total[i]
    after = new_sales.sum(axis=0)[i]
    diff = after - before
    print(f"  {name}: {int(before)} → {int(after)} triệu đồng (tăng {int(diff)} triệu đồng)")

# ============== 6. Lọc các ngày có doanh thu trên trung bình ==============
print("\n6. CÁC NGÀY CÓ DOANH THU LỚN HƠN MỨC TRUNG BÌNH TOÀN TUẦN")
print("-" * 70)
weekly_avg = daily_total.mean()
high_days = np.where(daily_total > weekly_avg)[0]

print(f"Doanh thu trung bình toàn tuần: {weekly_avg:.2f} triệu đồng/ngày")
print(f"\nCác ngày có doanh thu trên trung bình ({len(high_days)} ngày):")
for idx in high_days:
    diff = daily_total[idx] - weekly_avg
    print(f"  Ngày {idx+1}: {int(daily_total[idx])} triệu đồng (hơn trung bình {int(diff)} triệu đồng)")

# ============== 7. Tìm sản phẩm ổn định nhất (độ lệch chuẩn nhỏ nhất) ==============
print("\n7. SẢN PHẨM CÓ ĐỘ ỔN ĐỊNH CAO NHẤT (ĐỘ LỆCH CHUẨN NHỎ NHẤT)")
print("-" * 70)
product_std = sales.std(axis=0)
stable_product = np.argmin(product_std)

print(f"Độ lệch chuẩn doanh thu của từng sản phẩm:")
for i, name in enumerate(product_names):
    stability = "*** Ổn định nhất ***" if i == stable_product else ""
    print(f"  {name}: {product_std[i]:.2f} {stability}")

print(f"\nSản phẩm ổn định nhất: Sản phẩm {stable_product+1}")
print(f"  - Độ lệch chuẩn: {product_std[stable_product]:.2f}")
print(f"  - Giá trị tối thiểu: {sales[:, stable_product].min()}")
print(f"  - Giá trị tối đa: {sales[:, stable_product].max()}")
print(f"  - Phạm vi: {sales[:, stable_product].max() - sales[:, stable_product].min()}")

# ============== 8. Nhận xét về sản phẩm ưu tiên bán ==============
print("\n8. NHẬN XÉT VỀ SẢN PHẨM NÊN ƯU TIÊN BÁN")
print("-" * 70)

# Tính các chỉ số
print("\nPhân tích toàn diện:")
print("\nSắp xếp theo doanh thu tổng cộng:")
product_ranking = np.argsort(product_total)[::-1]
for rank, idx in enumerate(product_ranking, 1):
    print(f"  {rank}. Sản phẩm {idx+1}: {int(product_total[idx])} triệu đồng, "
          f"Độ lệch chuẩn: {product_std[idx]:.2f}")

print(f"\nSắp xếp theo độ ổn định (độ lệch chuẩn):")
stability_ranking = np.argsort(product_std)
for rank, idx in enumerate(stability_ranking, 1):
    print(f"  {rank}. Sản phẩm {idx+1}: Độ lệch chuẩn {product_std[idx]:.2f}, "
          f"Doanh thu: {int(product_total[idx])} triệu đồng")

# Top sản phẩm
top3_products = product_ranking[:3]

print(f"\n✓ TOP 3 SẢN PHẨM NÊN ƯU TIÊN BÁN:")
for rank, idx in enumerate(top3_products, 1):
    print(f"  {rank}. Sản phẩm {idx+1}")
    print(f"     - Doanh thu toàn tuần: {int(product_total[idx])} triệu đồng")
    print(f"     - Doanh thu trung bình: {product_mean[idx]:.2f} triệu đồng/ngày")
    print(f"     - Độ ổn định: {product_std[idx]:.2f}")

print(f"\n⚠ SẢN PHẨM CẦN CẢI THIỆN:")
worst_product = product_ranking[-1]
print(f"  - Sản phẩm {worst_product+1}: Doanh thu {int(product_total[worst_product])} triệu đồng")

print("\n" + "="*70)
print("KẾT LUẬN VÀ ĐỀ XUẤT")
print("="*70)
print(f"✓ Tập trung bán Sản phẩm {top3_products[0]+1} (doanh thu cao nhất)")
print(f"✓ Sản phẩm {stable_product+1} có doanh thu ổn định - thích hợp cho quy hoạch")
print(f"✓ Ngày {best_day+1} là ngày bán tốt nhất - có thể là ngày khuyến mãi hoặc sự kiện")
print(f"✓ Tăng quảng cáo cho Sản phẩm {worst_product+1} để cải thiện doanh thu")

