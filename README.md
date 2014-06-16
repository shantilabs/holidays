Красные дни календаря с учётом российских реалий.

```
from holidays import is_holiday

print datetime.date(2014, 1, 2).isoweekday()  # 4
print is_holiday(datetime.date(2014, 1, 2))  # False
print is_holiday(datetime.date(2014, 1, 2), 'ru')  # True
```
