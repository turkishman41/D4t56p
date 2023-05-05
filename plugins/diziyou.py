from pyrogram import Client, filters
import requests
import logging 
import pdfkit
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
import json

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup

async def diziyoum3u8getir(bot, message, url, say):
    for bolum in range(1, int(say)):
        urtemp = url.split("sezon-")[1]
        gitcek = urtemp.split("-")[0]
        uri = url.replace(f"{gitcek}", f"{bolum}")
        r = requests.get(uri)
        corba = BeautifulSoup(r.content, "lxml") 
        htmllinktemp = corba.find('iframe', attrs={"id":"diziyouPlayer"})
        htmllink = htmllinktemp.get("src")
        isimtemp = r.text.split("fas fa-play-circle")[1]
        isim1 = r.text.split("<")[1]
        isim = r.text.split("<")[0]  
        m3u8istek = requests.get(htmllink)
        m3u8corba = BeautifulSoup(m3u8istek.content, "lxml")
        texttemp = m3u8corba.find('source', attrs={"id":"diziyouSource"})
        text = texttemp.get("src")
        altyazilar = m3u8corba.findAll('track', attrs={"kind":"captions"})
        altmes = ""
        for a in altyazilar:
            alturl = a.get('src')
            altdil = a.get('label')
            altmes += f"Dil: {altdil}\nUrl: {alturl}\n\n"
        await message.reply_text(altmes)
        await message.reply_text(f"{text} | {bolum} Bölüm.mp4")
        doc = "plugins/star.py"
        await message.reply_document(doc)

@Client.on_message(filters.command('deneme'))
async def denemeurl(bot, message):
    try:
        mes = message.text.split(" ")
        url = mes[1]
        say = int(mes[2])
        say += 1
        await diziyoum3u8getir(bot, message, url, say)
    except Exception as e:
        await message.reply_text(e)
