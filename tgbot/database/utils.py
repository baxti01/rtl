import calendar
from collections import OrderedDict
from datetime import datetime, timedelta


def generate_monthly_dates(
        start_date: datetime,
        end_date: datetime
) -> dict[datetime, int]:
    current_date = datetime(
        year=start_date.year,
        month=start_date.month,
        day=1,
    )
    result = OrderedDict()

    while current_date <= end_date:
        result[current_date] = 0

        days_in_month = calendar.monthrange(
            current_date.year,
            current_date.month
        )[1]

        current_date += timedelta(days=days_in_month)

    return result


def generate_daily_dates(
        start_date: datetime,
        end_date: datetime
) -> dict[datetime, int]:
    current_date = datetime(
        year=start_date.year,
        month=start_date.month,
        day=1,
    )
    result = OrderedDict()

    while current_date <= end_date:
        result[current_date] = 0
        current_date += timedelta(days=1)

    return result


def generate_hourly_dates(
        start_date: datetime,
        end_date: datetime
) -> dict[datetime, int]:
    current_date = datetime(
        year=start_date.year,
        month=start_date.month,
        day=1,
    )
    result = OrderedDict()

    while current_date <= end_date:
        result[current_date] = 0
        current_date += timedelta(hours=1)

    return result


def generate_date_intervals(
        start_date: datetime,
        end_date: datetime
) -> dict[str, dict]:
    current_date = datetime(
        year=start_date.year,
        month=start_date.month,
        day=1,
    )
    monthly_intervals = OrderedDict()
    daily_intervals = OrderedDict()
    hourly_intervals = OrderedDict()

    while current_date <= end_date:
        monthly_date = datetime(
            year=current_date.year,
            month=current_date.month,
            day=1
        )
        daily_date = datetime(
            year=current_date.year,
            month=current_date.month,
            day=current_date.day
        )

        if not monthly_intervals.get(monthly_date, None):
            monthly_intervals[monthly_date] = 0

        if not daily_intervals.get(daily_date, None):
            daily_intervals[daily_date] = 0

        hourly_intervals[current_date] = 0

        current_date += timedelta(hours=1)

    return {
        'month': monthly_intervals,
        'day': daily_intervals,
        'hour': hourly_intervals
    }


generate_intervals_func_dict = {
    'month': generate_monthly_dates,
    'day': generate_daily_dates,
    'hour': generate_hourly_dates,
    'all': generate_date_intervals
}
