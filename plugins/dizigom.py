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

@Client.on_message(filters.command('dizigom'))
async def dizigom(bot, message):
    try:
        url = message.text.split(" ")[1]
        istek = requests.get(url) 
        corba = BeautifulSoup(istek.content, "lxml")
        LOGGER.info(corba)
        await message.reply_text(istek.url)
    except Exception as e:
        await message.reply_text(e)