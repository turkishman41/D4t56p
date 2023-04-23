from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging 
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
butonlar = InlineKeyboardMarkup([[InlineKeyboardButton(f'Bim Gelecek Hafta Salı', callback_data='bimges')]])

@Client.on_message(filters.command('fox'))
async def fox(bot, message):
    try:
        url = message.text.split(" ")[1]
        istek = requests.get(url) 
        corba = BeautifulSoup(istek.content, "lxml")
        LOGGER.info(corba)
        if 'videoSrc' in istek.text:
            temp = istek.text.split("videoSrc : '")[1]
            url = temp.split("'")[0]
            await message.reply_text(url)
        else:
            await message.reply_text("m3u8 Alamadım :(")
    except Exception as e:
        await message.reply_text(e)
