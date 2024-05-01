import datetime

import holidays


def count_working_hour_per_month(month, year):
    temp_date = datetime.datetime(year, month, 1).strftime("%B of %Y")

    if month == 12:
        days_in_month = datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)
    else:
        days_in_month = datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)
    print(f"{temp_date} has {days_in_month.days} days")

    working_h_per_month = 0

    for day in range(1, days_in_month.days + 1):
        date = datetime.date(year, month, day)
        if not is_holiday_or_weekend(date):
            working_h_per_month += 8
    return working_h_per_month


def is_holiday_or_weekend(date):
    return date.weekday() >= 5 or date in holidays.country_holidays("PL")


if __name__ == "__main__":
    print(count_working_hour_per_month(12, 2024))
