import asyncio
import logging
import telegram

from utils.common import read_token

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    TOKEN = read_token()
    bot = telegram.Bot(TOKEN)
    async with bot:
        logger.info(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
