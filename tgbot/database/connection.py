from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorClient

from tgbot.config import config
from tgbot.database.filters import date_interval_filter
from tgbot.database.utils import generate_intervals_func_dict

client = AsyncIOMotorClient(config.db_url)

db = client.sampleDB


async def get_data_from_db(
        start_date: datetime,
        end_date: datetime,
        group_type: str
) -> dict[datetime, int]:
    pipeline = [
        {
            '$match': {'dt': {'$gte': start_date, '$lte': end_date}}
        },
        {
            '$group': {
                '_id': {'$dateFromParts': date_interval_filter[group_type]},
                'total': {'$sum': '$value'},
            }
        },
        {
            '$sort': {'_id': 1}
        },
        {
            '$group': {
                '_id': 0,
                'labels': {'$push': '$_id'},
                'dataset': {'$push': '$total'},
            }
        },
        {
            '$project': {
                '_id': 0,
                'dataset': 1,
                'labels': 1,
            }
        },
    ]

    return await db.sample_collection.aggregate(pipeline).next()


async def format_result(
        data: dict,
        template: dict
) -> dict[str, list]:
    for total, date in zip(data['dataset'], data['labels']):
        template[date] = total

    result = {
        'dataset': list(template.values()),
        'labels': list(template.keys())
    }
    return result


async def get_payments(
        start_date: datetime,
        end_date: datetime,
        group_type: str
) -> dict[str, list]:
    generate_intervals_func = generate_intervals_func_dict[group_type]

    data_from_db = await get_data_from_db(start_date, end_date, group_type)
    intervals = generate_intervals_func(start_date, end_date)

    return await format_result(
        data_from_db,
        intervals
    )
