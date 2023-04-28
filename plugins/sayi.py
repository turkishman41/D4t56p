# :d tarafından mamaklı için yazılmıştır.
# Sayı Tahmin Oyunu
from pyrogram import Client, filters
from pyromod import listen
import random

async def sayitahmin(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "Merhaba Dostum 1-100 arası tuttuğum sayıyı bul bakalım..") # Oyuncudan Sayı istendi..
    kere += 1 # kere'ye +1 ekletildi çünkü yukarda bir tahmin edildi.
    await tahmingetir(bot, message, tahmin, secilensayi, kere) # Tahmin edilen sayıyı seçilen sayıyla karşılaştırmak için bir fonksiyon yazıldı.
    
async def tahmingetir(bot, message, tahmin, secilensayi, kere):
    try:
        text = tahmin.text # Tahmin texti alındı
        if not text.isdigit(): # Sayı mı Kelime mi kontrol edildi. 
            await sohbetediliyor(bot, message, secilensayi, kere) # Kelimeyse tekrar tahmin mesajı gönderildi. 
        elif int(text) == int(secilensayi): # tahmin edilen sayı seçilen sayıyla aynı mı diye kontrol edildi. 
            await bot.send_message(message.chat.id, f"Tebrikler Doğru Cevap: {secilensayi}\n{kere} deneyişte Buldun") # Doğru bilme mesajı attırıldı..
        elif int(text) > int(secilensayi): # tahmin edilen seçilenden büyük mü diye kontrol edildi.
            await buyuktahmin(bot, message, secilensayi, kere)
        elif int(text) < int(secilensayi): # Tahmin edilen seçilen sayıdan küçük mü kontrol edildi. 
            await kucuktahmin(bot, message, secilensayi, kere)

    except Exception as e:
        await message.reply_text(e)
        
async def sohbetediliyor(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "Lütfen Oyun Oynanırken Sohbet Etmeyin 😡") # Yeni bir tahmin mesajı uyatı biçiminde gönderildi.
    kere +=1
    await tahmingetir(bot, message, tahmin, secilensayi, kere)
    
async def buyuktahmin(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "Çok Söyledin aşağıya in")
    kere +=1
    await tahmingetir(bot, message, tahmin, secilensayi, kere)

async def kucuktahmin(bot, message, secilensayi, kere):
    tahmin = await bot.ask(message.chat.id, "az Söyledin yukarı çık")
    kere +=1
    await tahmingetir(bot, message, tahmin, secilensayi, kere)

@Client.on_message(filters.command('sayi'))
async def sayioyun(bot, message):
    try:
        secilensayi = random.randint(1, 100) # 1 ile 100 arasında sayı seçtiriliyor.
        kere = 0 # kaç kere de bilindiğini yazdırmak için int olarak bri değişken oluşturuldu
        await sayitahmin(bot, message, secilensayi, kere) # Sayı Tahmin döngüsü bailatıldı.
    except Exception as e:
        await message.reply_text(e)
