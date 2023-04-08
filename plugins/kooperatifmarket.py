from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
butonlar = InlineKeyboardMarkup([[InlineKeyboardButton(f'Bim Gelecek Hafta Salı', callback_data='bimges')]])

@Client.on_message(filters.command('koop'))
async def koop(bot, message):
    try:
        url = "https://www.akakce.com/brosurler/kooperatifmarket-15-mart-2023-aktuel-katalogu-firsat-indirim-26738"
        i = requests.get(url)
        corba = BeautifulSoup(i.content, "lxml")
        LOGGER.info(corba)
    except Exception as e:
        await message.reply_text(e)
