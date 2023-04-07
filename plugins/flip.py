# Coded by @mmagneto (:d) 

from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command('flip'))
async def flip5(bot, message):
    try:
        mestemp = message.text.split(" ")
        kitap = mestemp[1]
        say = 1
        while True:
            url = f"http://online.fliphtml5.com/{kitap}/files/large/{say}.jpg"
            dosyam = f"{say}.jpg"
            say += 1 
            r = requests.get(url)
            with open(dosyam, "wb") as f:
                f.write(r.content)
            await message.reply_photo(dosyam)
    except Exception as e:
        await message.reply_text(e)
