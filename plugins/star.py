from pyrogram import Client, filters
import requests
import logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
import json

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
            bolsay = url.split("/")[7]
            for bolum in range(1, sayi):
                uri = url.replace(str(bolsay), f"{bolum}-bolum") 
                await message.reply_text(uri) 
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
                    urltemp = jso['data']['flavors']['0']['file_url_1']
                    url = urltemp.replace("playlist", isim)
                    await message.reply_text(url)
                else:
                    await message.reply_text(f"{bolum}. için m3u8 Alamadım :(")
    except Exception as e:
        await message.reply_text(e) 
