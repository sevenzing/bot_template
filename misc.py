from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logging

from modules.common.config import constants


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -15s %(funcName) -20s: %(message)s')
LOG_LEVEL = logging.DEBUG if constants.LOG_LEVEL == 'debug' else logging.INFO if constants.LOG_LEVEL == 'info' else logging.ERROR
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

storage = RedisStorage2(**constants.redis)

engine = create_engine(constants.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


bot = Bot(token=constants.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)


