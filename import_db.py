import asyncio

from bson import decode_all
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from pymongo.errors import BulkWriteError

from tgbot.config import config


async def import_collection(collection: Collection) -> bool:
    with open('sample_collection.bson', 'rb') as f:
        data = decode_all(f.read())
    try:
        await collection.insert_many(data)
    except BulkWriteError:
        return False

    return True


if __name__ == '__main__':
    client = AsyncIOMotorClient(config.db_url)
    db = client.sampleDB
    asyncio.run(import_collection(db.sample_collection))
