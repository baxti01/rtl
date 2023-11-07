import asyncio
import logging

from aiogram import Bot, Dispatcher

from tgbot.config import config
from tgbot.handlers.amounts_payments import amounts_payments_router


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d "
               "#%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging()

    bot = Bot(token=config.bot_token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(amounts_payments_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот был выключен!")
