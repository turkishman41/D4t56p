# Coded by @mmagneto (:d) 

from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup
import logging

async def dizilinkgetir(bot, message, dizipalurltemp, say):
    try:
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
        with open(m3u8file, 'w') as dosya:
               dosya.write(''.join(text))  
        await message.reply_document(m3u8file)
    except Exception as e:
        await message.reply_text(e)

async def filmlinkgetir(bot, message, dizipalurltemp):
    try:
        istek = requests.get(dizipalurltemp)
        corba = BeautifulSoup(istek.content, "lxml")
        g = corba.find('div', attrs={"class":"video-banner"})
        d = g.find("iframe")
        link = d.get("src")
        y = requests.get(link)
        p = y.text.split('file:"')
        m3u8 = p[1].split('"')[0]
        text = f'Kaynak Url: {dizipalurltemp}\nM3u8: {m3u8}\n\n'
        tex = f"{dizipalurltemp}\n\n`{m3u8}`"
        await message.reply_text(tex)
        adtemp = dizipalurltemp.split(".com/")[1]
        ad = adtemp.split("/")[0] 
        m3u8file = f"{ad} Dizipal M3u8 Linkleri.txt"
        with open(m3u8file, 'w') as dosya:
               dosya.write(''.join(text))  
        await message.reply_document(m3u8file)
    except Exception as e:
        await message.reply_text(e)

async def diziteklinkgetir(bot, message, dizipalurltemp):
    try:
        istek = requests.get(dizipalurltemp)
        corba = BeautifulSoup(istek.content, "lxml")
        g = corba.find('div', attrs={"class":"video-banner"})
        d = g.find("iframe")
        link = d.get("src")
        y = requests.get(link)
        p = y.text.split('file:"')
        m3u8 = p[1].split('"')[0]
        text = f'Kaynak Url: {dizipalurltemp}\nM3u8: {m3u8}\n\n'
        tex = f"{dizipalurltemp}\n\n`{m3u8}`"
        await message.reply_text(tex)
        adtemp = dizipalurltemp.split("dizi/")[1]
        ad = adtemp.split("/")[0] 
        m3u8file = f"{ad} Dizipal M3u8 Linkleri.txt"
        with open(m3u8file, 'w') as dosya:
               dosya.write(''.join(text))  
        await message.reply_document(m3u8file)
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('dizipal'))
async def dizipaldizilink(bot, message):
    try:
        urltemp = message.text.split(" ")
        dizipalurltemp = urltemp[1]
        say = urltemp[2]
        await dizilinkgetir(bot, message, dizipalurltemp, say)
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('tekdizipal'))
async def dizipaldiziteklink(bot, message):
    try:
        urltemp = message.text.split(" ")
        dizipalurltemp = urltemp[1]
        await diziteklinkgetir(bot, message, dizipalurltemp)
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('filmpal'))
async def dizipalfilmlink(bot, message):
    try:
        urltemp = message.text.split(" ")
        dizipalurltemp = urltemp[1]
        await filmlinkgetir(bot, message, dizipalurltemp)
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('dizigom'))
async def dizigom(bot, message):
    try:
        urltemp = message.text.split(" ")
        url = urltemp[1]
        r = requests.get(url)
        c = BeautifulSoup(r.content, "lxml")
        LOGGER.info(c)
    except Exception as e:
        await message.reply_text(e)
