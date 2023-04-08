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
        proxy = "http://ebf4eec57ff82dd93e49e244671fe88c67bf0168:antibot=true@proxy.zenrows.com:8001"
        proxies = {"http": proxy, "https": proxy}
        i = requests.get(url, proxies=proxies, verify=False)
        embedtemp = i.content.split('"contentUrl":"')[1]
        embed = embedtemp.split('"')[0]
        text = embed.replace("\/", "/")
        await message.reply_text(text)
        LOGGER.info(corba)
    except Exception as e:
        await message.reply_text(e)
