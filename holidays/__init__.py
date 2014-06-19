import datetime
import os


ONE_DAY = datetime.timedelta(days=1)
ONE_WEEK = datetime.timedelta(7)


def get_workday(dt, country_code=None):
    """
    >>> get_workday(datetime.date(2014, 1, 1), 'ru')
    datetime.date(2014, 1, 8)
    """
    while is_holiday(dt, country_code):
        dt += ONE_DAY
    return dt


def get_monday(dt):
    while dt.isoweekday() != 1:
        dt -= ONE_DAY
    return dt


def get_week_number(dt):
    return int(dt.strftime('%W'))


def is_holiday(dt, country_code=None):
    """
    >>> is_holiday(datetime.date(2014, 4, 1))
    False
    >>> # workday
    >>> is_holiday(datetime.date(2014, 1, 1))
    False
    >>> # russian holiday
    >>> is_holiday(datetime.date(2014, 1, 1), 'ru')
    True
    >>> # no data
    >>> is_holiday(datetime.date(1900, 1, 1), 'ru')
    False
    """
    if country_code is None:
        return naive_is_holiday(dt)

    key = (country_code, dt.year)
    if key in _cache:
        arr = _cache[key]
    else:
        arr = _cache[key] = _read_data(*key)

    if arr:
        return arr[dt.timetuple().tm_yday]

    return naive_is_holiday(dt, country_code)


def naive_is_holiday(dt, country_code=None):
    return dt.isoweekday() in (6, 7)


def iter_year(year):
    """
    >>> list(iter_year(2000))[0]
    datetime.date(2000, 1, 1)
    >>> list(iter_year(2000))[-1]
    datetime.date(2000, 12, 31)
    """
    dt = datetime.date(year, 1, 1)
    prev_dt = dt
    while dt.year == prev_dt.year:
        yield dt
        prev_dt = dt
        dt += ONE_DAY


holiday_char = 'x'
workday_char = '.'
valid_chars = (holiday_char, workday_char)

_cache = {}
_datadir = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'data')


def _read_data(country_code, year):
    path = '{0}/{1}/{2}.txt'.format(
        _datadir,
        country_code,
        year,
    )
    return [
        char == holiday_char
        for char in open(path).read()
        if char in valid_chars
    ] if os.path.exists(path) else None


def main():
    import sys

    if '--test' in sys.argv:
        import doctest
        doctest.testmod()
        sys.exit(0)

    if len(sys.argv) != 2:
        sys.stdout.write('Usage: %s <year>\n')
        sys.exit(1)
    line = ''
    year = int(sys.argv[1])
    for dt in iter_year(year):
        prev_dt = dt - ONE_DAY
        if dt.month != prev_dt.month or dt == prev_dt:
            if line:
                sys.stdout.write('{0}\n'.format(line))
                line = ''
            sys.stdout.write('# {0}.{1}\n'.format(dt.month, dt.year))
            line = ' ' * (dt.isoweekday() - 1)
        line += holiday_char if is_holiday(dt) else workday_char
        if dt.isoweekday() >= 7:
            sys.stdout.write('{0}\n'.format(line))
            line = ''


if __name__ == '__main__':
    main()
