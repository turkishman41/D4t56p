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

@Client.on_message(filters.command('star'))
async def star(bot, message):
    try:
        mes = message.text.split(" ")
        if len(mes) < 3:
            await message.reply_text("Yanlış Kullanım doğru kullanım:\n\n/fox https://www.fox.com.tr/Darmaduman/bolum/1 9")
        else:
            url = mes[1]
            say = int(mes[2])
            sayi = say + 1
            if 'arsiv' in url:
                bolsay = url.split("/")[7]
            else:
                bolsay = url.split("/")[6]
            for bolum in range(1, sayi):
                uri = url.replace(str(bolsay), f"{bolum}-bolum") 
                r = requests.get(uri) 
                if '\rvar videoDataList' in r.text:
                    temp = r.text.split('\rvar videoDataList')[1]
                    urtemp = temp.split('"videoUrl": "')[1]
                    ur = urtemp.split('"')[0]
                    idtemp = temp.split('"m3u8VideoId": "')[1]
                    id = idtemp.split('"')[0]
                    url1 = f"{ur}&m3u8VideoId={id}&totalPartCount=1"
                    t = requests.get(url1)
                    jso = t.json()
                    LOGGER.info(jso)
                    title = jso['data']['filename']
                    isim = title.split("/")[3]
                    urltemp = jso['data']['flavors']['hds']
                    urll = urltemp.replace("playlist", "chunklist_b600000")
                    if '.mp4' in isim:
                        await message.reply_text(f"{urll} | {isim}")
                    else:
                        await message.reply_text(f"{urll} | {isim}.mp4") 
                else:
                    await message.reply_text(f"{bolum}. için m3u8 Alamadım :(")
    except Exception as e:
        await message.reply_text(e) 

@Client.on_message(filters.command('pdf'))
async def htmltopdf(bot, message):
    try:
        filehtml = await bot.download_media(
                       message=message.reply_to_message,
                       file_name='htmlfile.html') 
        splitpath = filehtml.split("/downloads/")
        dow_file_name = splitpath[1]
        file =f"downloads/{dow_file_name}"
        pdfkit.from_file(file, 'out.pdf')
        document = "out.pdf"
        await message.reply_document(document) 
    except Exception as e:
        await message.reply_text(e)


