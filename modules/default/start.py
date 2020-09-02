from aiogram import types
import logging

from modules.default import messages
from modules.database.models import User

from misc import session

async def cmd_start(message: types.Message):
    '''
    Conversation's entry point. Send start message
    '''

    await message.answer(messages.ON_CMD_START)
