from pyrogram import Client, filters
from pyromod import listen
import random



async def sayitahmin(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "Merhaba Dostum 1-100 arası tuttuğum sayıyı bul bakalım..")
    kere += 1
    await tahmingetir(bot, message, tahmin, secilensayi, kere)
    
async def tahmingetir(bot, message, tahmin, secilensayi, kere):
    try:
        sayisi = int(tahmin)
        if sayisi == int(secilensayi):
            await bot.send_message(message.chat.id, f"Tebrikler {kere} deneyişte Buldun") 
        elif sayisi > int(secilensayi):
            await buyuktahmin(bot, message, secilensayi, kere)
        elif sayisi < int(secilensayi):
            await kucuktahmin(bot, message, secilensayi, kere)

    except:
        await sohbetediliyor(bot, message, secilensayi, kere)
        
async def sohbetediliyor(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "Lütfen Oyun Oynanırken Sohbet Etmeyin 😡")
    kere +=1
    await tahmingetir(bot, message, tahmin, secilensayi)
    
async def buyuktahmin(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "Çok Söyledin aşağıya in")
    kere +=1
    await tahmingetir(bot, message, tahmin, secilensayi)

async def kucuktahmin(bot, message, secilensayi, kere):

    tahmin = await bot.ask(message.chat.id, "az Söyledin yukarı çık")

    kere +=1

    await tahmingetir(bot, message, tahmin, secilensayi)

 
    

    

   
 
    
    
@Client.on_message(filters.command('sayi'))
async def sayioyun(bot, message):
    try:
        secilensayi = random.randint(1, 100)
        kere = 0
        await sayitahmin(bot, message, kere, secilensayi)
    except Exception as e:
        await message.reply_text(e)
