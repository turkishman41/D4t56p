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

sporxcanli = "https://m.sporx.com/canliskorlar/"

async def skorlar(bot, message):
    istek = requests.get(sporxcanli)
    corbam = BeautifulSoup(istek.content, "lxml")
    jsontemp = istek.text.split("jsonData = [")[1]
    jsonum = jsontemp.split("]")[0]
    text = json.dumps(jsonum)

    LOGGER.info(text)
    await message.reply_text(text)
    
@Client.on_message(filters.command('skor'))
async def skorgetir(bot, message):
    try:
        skor = await skorlar(bot, message)
    except Exception as e:
        await message.reply_text(f"hata: {e}")
