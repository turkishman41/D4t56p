# Coded by @mmagneto (:d) 

from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging
import telegraph
from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name='Dizipal Bot')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
butonlar = InlineKeyboardMarkup([[
           InlineKeyboardButton(f'A101 Bu Hafta Aldın Aldın', callback_data='buhaftaaldin')],
           [InlineKeyboardButton(f'A101 Gelecek Hafta Aldın Aldın', callback_data='gelecekhaftaaldin')
           ],[
           InlineKeyboardButton(f'A101 Haftanın Yıldızları', callback_data='haftayildiz')],
           [InlineKeyboardButton(f'A101 Hadi Fırsatları', callback_data="hadi")
           ],[
           InlineKeyboardButton(f'A101 Genel Kampanya', callback_data="a101genel")
           ]]) 

async def aldinaldingelecekhafta(bot, message):
    try:
        url = "https://www.a101.com.tr/aldin-aldin-gelecek-hafta-brosuru"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "Aldın Aldın Gelecek Hafta Broşürleri Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

async def haftaninyildizlari(bot, message):
    try:
        url = "https://www.a101.com.tr/afisler-haftanin-yildizlari"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "Haftanın Yıldızları Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

async def a101genel(bot, message):
    try:
        url = "https://www.a101.com.tr/buyuk-oldugu-icin-ucuz-afisler"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "A101 Genel Kampanyaları Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e) 

async def a101hadi(bot, message):
    try:
        url = "https://www.a101.com.tr/afisler-hadi"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "A101 Hadi Fırsatları Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

async def aldinaldinbuhafta(bot, message):
    try:
        url = "https://www.a101.com.tr/aldin-aldin-bu-hafta-brosuru"
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        afislerr = c.findAll('img', attrs={"class":"image0"})
        fotolar = []
        for foto in afislerr:
            photo = foto.get('src')
            fotolar.append(photo)
        for brosur in fotolar:
            await bot.send_photo(
                chat_id = message.from_user.id,
                photo = brosur)
        await bot.send_message(message.from_user.id, "Aldın Aldın Bu Hafta Broşürleri Başarıyla Getirildi..") 
    except Exception as e:
        await bot.send_message(message.from_user.id, e)

@Client.on_message(filters.command('a101') & filters.private)
async def a101getir(bot, message):
    try:
       text = f"Merhaba {message.from_user.mention},\nAşağıdaki butonlardan hangi Broşürleri istediğini seç 😊"
       await bot.send_message(
           chat_id = message.chat.id,
           text = text,
           reply_markup = butonlar)
    except Exception as e:
        await message.reply_text(e)

@Client.on_callback_query(filters.regex('^buhaftaaldin$'))
async def aldinaldinbugetir(bot, message):
    await message.answer("Bu Hafta Aldın Aldın Broşürleri Getiriliyor...",
                         show_alert=True)
    await aldinaldinbuhafta(bot, message)

@Client.on_callback_query(filters.regex('^gelecekhaftaaldin$'))
async def aldinaldingelecekgetir(bot, message):
    await message.answer("Gelecek Hafta Aldın Aldın Broşürleri Getiriliyor...",
                         show_alert=True)
    await aldinaldingelecekhafta(bot, message)

@Client.on_callback_query(filters.regex('^haftayildiz$'))
async def haftaninyildizlarigetir(bot, message):
    await message.answer("Haftanın Yıldızları Getiriliyor...",
                         show_alert=True)
    await haftaninyildizlari(bot, message)

@Client.on_callback_query(filters.regex('^hadi$'))
async def a101hadigetir(bot, message):
    await message.answer("A101 Hadi Fırsatları Getiriliyor...",
                         show_alert=True)
    await a101hadi(bot, message)

@Client.on_callback_query(filters.regex('^a101genel$'))
async def a101genelgetir(bot, message):
    await message.answer("A101 Genel Kampanyalar Getiriliyor...",
                         show_alert=True)
    await a101genel(bot, message)

@Client.on_message(filters.command('dizipal'))
async def dizipallink(bot, message):
    try:
        urltemp = message.text.split(" ")
        dizipalurltemp = urltemp[1]
        say = urltemp[2]
        sayi = int(say)+ 1
        text = f""
        for a in range(1, sayi):
            uri = dizipalurltemp.split("bolu")
            t = f"m-{a}"
            url = dizipalurltemp.replace(str(uri[1]), t)
            istek = requests.get(url)
            corba = BeautifulSoup(istek.content, "lxml")
            g = corba.find('div', attrs={"class":"video-banner"})
            d = g.find("iframe")
            link = d.get("src")
            y = requests.get(link)
            p = y.text.split('file:"')
            m3u8 = p[1].split('"')[0]
            text += f'Kaynak Url: {url}\nM3u8: {m3u8}\n\n'
            tex = f"{url}\n\n`{m3u8}`"
            await message.reply_text(tex)
        adtemp = dizipalurltemp.split("dizi/")[1]
        ad = adtemp.split("/")[0] 
        m3u8file = f"{ad} Dizipal M3u8 Linkleri.txt"
        with open(m3u8file) as dosya:
               dosya.write(''.join(text))  
        await message.reply_document(m3u8file)
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('log'))
async def log_handler(bot, message):
    with open('log.txt', 'rb') as f:
        try:
            await bot.send_document(document=f,
                                  file_name=f.name, reply_to_message_id=message.id,
                                  chat_id=message.chat.id, caption=f.name)
        except Exception as e:
            await message.reply_text(str(e))
