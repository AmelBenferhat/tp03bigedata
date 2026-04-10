import pandas as pd

# تحميل البيانات
data = pd.read_csv('test.csv')

# عرض أول 5 أسطر
print(data.head())

# معلومات عامة
print(data.info())