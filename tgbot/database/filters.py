date_type_with_month = {
    'year': {'$year': '$dt'},
    'month': {'$month': '$dt'},
    'day': 1,
    'hour': 0
}

date_type_with_day = {
    'year': {'$year': '$dt'},
    'month': {'$month': '$dt'},
    'day': {'$dayOfMonth': '$dt'},
    'hour': 0
}
date_type_with_hour = {
    'year': {'$year': '$dt'},
    'month': {'$month': '$dt'},
    'day': {'$dayOfMonth': '$dt'},
    'hour': {'$hour': '$dt'}
}

date_interval_filter = {
    'month': date_type_with_month,
    'day': date_type_with_day,
    'hour': date_type_with_hour
}
