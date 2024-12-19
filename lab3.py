import pandas as pd

#LAB 3.1. KHÁM PHÁ DỮ LIỆU.
stocks1 = pd.read_csv(r'G:\HUNG\bai_tap_thuc_hanh\lab3\stocks1.csv')

# 1. Hiển thị 5 dòng đầu tiên
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

# 2. Hiển thị kiểu dữ liệu của mỗi cột
print("\nKiểu dữ liệu của mỗi cột trong stocks1:")
print(stocks1.dtypes)

# 3. Xem thông tin tổng quan
print("\nThông tin tổng quan về stocks1:")
print(stocks1.info())


#LAB 3.2. XỬ LÝ DỮ LIỆU NULL

import pandas as pd

# Kiểm tra dữ liệu Null
print("Kiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())

# Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
stocks1['high'] = stocks1['high'].fillna(stocks1['high'].mean())

# Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
stocks1['low'] = stocks1['low'].fillna(stocks1['low'].mean())

# Hiển thị thông tin tổng quan sau khi xử lý dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
print(stocks1.info())

#LAB 3.3. GỘP DỮ LIỆU VÀ PHÂN TÍCH CƠ BẢN

# 1. Đọc file stocks2.csv vào DataFrame
stocks2 = pd.read_csv(r'G:\HUNG\bai_tap_thuc_hanh\lab3\stocks2.csv')


# 2. Gộp stocks1 và stocks2 thành DataFrame mới
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày
average_prices = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

# 4. Hiển thị 5 dòng đầu tiên của kết quả
print("\n5 dòng đầu tiên của giá trung bình:")
print(average_prices.head())

#LAB 3.4. GỘP DỮ LIỆU VÀ PHÂN TÍCH CƠ BẢN

# Đọc file companies.csv vào DataFrame
companies = pd.read_csv(r'G:\HUNG_23174600114\1\lab3\companies.csv')

# 1. Hiển thị 5 dòng đầu tiên của companies
print("\nThông tin tổng quan về companies:")
print(companies.info())

print("\n5 dòng đầu tiên của companies:")
print(companies.head())

# 2. Kết hợp stocks và companies dựa trên cột symbol
merged_data = stocks.merge(companies, left_on='symbol', right_on='name', how='inner')

# 3. Tính giá đóng cửa trung bình cho mỗi công ty
average_close = merged_data.groupby('name')['close'].mean()

# 4. Hiển thị kết quả cho 5 công ty đầu tiên
print(average_close.head())

#LAB 3.5: SỬ DỤNG MULTIINDEX VÀ GROUPBY

# 1. Tạo MultiIndex từ cột date và symbol
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Tính giá trung bình và volume trung bình
grouped = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',
    'high': 'mean',
    'low': 'mean',
    'close': 'mean',
    'volume': 'mean'
})

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
sorted_grouped = grouped.sort_index()

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print(sorted_grouped.head())

#LAB 3.6: TẠO VÀ PHÂN TÍCH PIVOT TABLE

# 1. Tạo Pivot Table với close trung bình
pivot_table = stocks.pivot_table(
    values='close', 
    index='date', 
    columns='symbol', 
    aggfunc='mean'
)

# 2. Thêm một cột tính tổng volume giao dịch
pivot_table['Total Volume'] = stocks.groupby('symbol')['volume'].sum()

# 3. Sắp xếp Pivot Table dựa trên tổng volume giao dịch
sorted_pivot = pivot_table.sort_values(by='Total Volume', ascending=False)

# 4. Hiển thị 5 mã chứng khoán có tổng volume giao dịch cao nhất
print(sorted_pivot.head())







