import json
from datetime import datetime

from aiogram import Router, types
from pydantic import BaseModel

from tgbot.database.connection import get_payments

amounts_payments_router = Router(
    name='amounts_payments_router'
)


class InputData(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: str


@amounts_payments_router.message()
async def get_amounts_payments(message: types.Message):
    input_data = InputData.model_validate_json(message.text)

    data: dict = await get_payments(
        input_data.dt_from,
        input_data.dt_upto,
        input_data.group_type
    )

    await message.answer(str(data))
