Красные дни календаря с учётом российских реалий.

Установка:
```bash
pip install -e git://github.com/shantilabs/holidays.git#egg=holidays
```

Использование:
```python
from holidays import is_holiday, get_workday

print(datetime.date(2014, 1, 2).isoweekday())  # 4
print(is_holiday(datetime.date(2014, 1, 2)))  # False
print(is_holiday(datetime.date(2014, 1, 2), 'ru'))  # True
print(get_workday(datetime.date(2014, 1, 2), 'ru'))  # datetime.date(2014, 1, 8)
```

Генерация шаблона для года:
```bash
python holidays/__init__.py 2021 > holidays/data/ru/2021.txt
```