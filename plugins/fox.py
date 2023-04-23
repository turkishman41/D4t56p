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

@Client.on_message(filters.command('fox'))
async def fox(bot, message):
    try:
        mes = message.text.split(" ")
        if len(mes) < 3:
            await message.reply_text("Yanlış Kullanım doğru kullanım:\n\n/fox https://www.fox.com.tr/Darmaduman/bolum/1 9")
        else:
            url = mes[1]
            say = int(mes[2])
            sayi = say + 1
            for bolum in range(1, sayi):
                bolsay = url.split("bolum/")[1]
                uri = url.replace(str(bolsay), str(bolum))
                istek = requests.get(uri) 
                if 'videoSrc' in istek.text:
                    temp = istek.text.split("videoSrc : '")[1]
                    text = temp.split("'")[0]
                    await message.reply_text(f"{bolum}. Bölüm için m3u8: {text}")
                else:
                    await message.reply_text(f"{bolum}. için m3u8 Alamadım :(")
    except Exception as e:
        await message.reply_text(e)
