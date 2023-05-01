from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging 
import json
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

skorurl = "https://www.flashscore.com.tr/futbol/turkiye/super-li-g/#/lh8AshXk/table/overall"

async def skorlar(bot, message):
    istek = requests.get(skorurl)
    corba = BeautifulSoup(istek.content, "html.parser")
    tablo = corba.find('table', {'class': 'soccer'})
    LOGGER.info(tablo)
    LOGGER.info(corba)
    await message.reply_text(tablo)
    
@Client.on_message(filters.command('skor'))
async def skorgetir(bot, message):
    try:
        skor = await skorlar(bot, message)
    except Exception as e:
        await message.reply_text(f"hata: {e}")
