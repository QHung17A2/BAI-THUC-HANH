# LAB 2.1: Phân tích dữ liệu khí hậu sử dụng numpy
import numpy as np

# Tạo dữ liệu nhiệt độ
temperatures = np.round(np.random.uniform(15, 35, 30), 2)
print("Nhiệt độ hàng ngày trong tháng:", temperatures)
print("Nhiệt độ trung bình trong tháng:", np.mean(temperatures))

# Xác định xu hướng nhiệt độ
max_temp_day = np.argmax(temperatures) + 1
min_temp_day = np.argmin(temperatures) + 1
print(f"Nhiệt độ cao nhất vào ngày {max_temp_day}, thấp nhất vào ngày {min_temp_day}")

temp_diff = np.diff(temperatures)
max_diff_day = np.argmax(np.abs(temp_diff)) + 1
print(f"Ngày có biến đổi nhiệt độ cao nhất là ngày {max_diff_day}")

# Fancy indexing
above_20 = temperatures[temperatures > 20]
days_5_10_15_20_25 = temperatures[[4, 9, 14, 19, 24]]
above_avg = temperatures[temperatures > np.mean(temperatures)]
even_days = temperatures[1::2]
odd_days = temperatures[0::2]

print("Nhiệt độ > 20°C:", above_20)
print("Nhiệt độ ngày 5, 10, 15, 20, 25:", days_5_10_15_20_25)
print("Nhiệt độ trên trung bình:", above_avg)
print("Nhiệt độ ngày chẵn:", even_days)
print("Nhiệt độ ngày lẻ:", odd_days)