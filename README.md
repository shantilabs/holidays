Красные дни календаря с учётом российских реалий.

Установка:
```
pip install -e git://github.com/shantilabs/holidays.git#egg=holidays
```

Использование:
```
from holidays import is_holiday, get_workday

print datetime.date(2014, 1, 2).isoweekday()  # 4
print is_holiday(datetime.date(2014, 1, 2))  # False
print is_holiday(datetime.date(2014, 1, 2), 'ru')  # True

print get_workday(datetime.date(2014, 1, 2), 'ru')  # datetime.date(2014, 1, 8)
```
