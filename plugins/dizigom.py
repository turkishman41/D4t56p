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

ac = requests.Session()
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        }

@Client.on_message(filters.command('dizigom'))
async def dizigom(bot, message):
    try:
        url = message.text.split(" ")[1]
        i = selenium.get(url) 
        embedtemp = i.text.split('"contentUrl":"')[1]
        embed = embedtemp.split('"')[0]
        u = embed.replace("\/", "/")
        await message.reply_text(u)
        istek = selenium.get(u)
        corba = BeautifulSoup(istek.content, "lxml")
        LOGGER.info(corba)
        await message.reply_text(istek.url)
    except Exception as e:
        await message.reply_text(e)
