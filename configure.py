from typing import Final
import tg
import mongodb

MONGODB_TOKEN: Final = ' ... '
TELEGRAM_TOKEN: Final = ' ... '

def init():
    tg._init_(TELEGRAM_TOKEN)
    mongodb._init_(MONGODB_TOKEN)

init()

