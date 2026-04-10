import pandas as pd

# 1️⃣ قراءة الملف
data = pd.read_csv(r'C:\Users\DELL\Desktop\big data\test.csv')

# 2️⃣ تنظيف البيانات
data_cleaned = data.dropna()   # حذف القيم الفارغة

# 3️⃣ حفظ الملف الجديد
data_cleaned.to_csv(r'C:\Users\DELL\Desktop\big data\test_cleaned.csv', index=False)

print("تم إنشاء الملف الجديد بنجاح ✅")