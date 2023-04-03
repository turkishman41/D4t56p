from pyrogram import Client, filters

@Client.on_message(filters.command('start'))
async def startmesaj(bot, message):
    try:
        await message.reply_text(f"Merhaba {message.from_user.mention}\nBeni Kullanarak Zincir Market Broşürlerine Ulaşabilirsin.\n\nKomutlar:\n/bim\n/a101\n/sok\n/migros")
    except Exception as e:
        await message.reply_text(e)
