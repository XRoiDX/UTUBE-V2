from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⛄Cʜᴀɴɴᴇʟ", url="https://t.me/XRoid_BotZ"), InlineKeyboardButton("⛄Cʀᴇᴀᴛᴏʀ", url="https://t.me/Space4AFML") ],
        [InlineKeyboardButton(
            "⛄ Jᴏɪɴ ɴᴏᴡ ⛄", url="https://t.me/XRoid_BotZ")]
    ])
    
    welcomed = f"""Hᴇʏ <b>{message.from_user.first_name}</b>\n\nA Sɪᴍᴘʟᴇ Yᴏᴜᴛᴜʙᴇ Dᴏᴡɴʟᴏᴀᴅᴇʀ Bᴏᴛ Tʜᴀᴛ Cᴀɴ:
  ➠ Dᴏᴡɴʟᴏᴀᴅ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏs
  ➠ Dᴏᴡɴʟᴏᴀᴅ Aᴜᴅɪᴏ Fʀᴏᴍ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏs \n\n Mᴀᴅᴇ Wɪᴛʜ ♥️ Bʏ <a href="https://telegra.ph/file/e981d066dc5b3b2525c5c.jpg">XRoiD_ʙᴏᴛs</a>
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ: <a href="https://t.me/Space4AFML">メ™Aʟꜰʀᴇᴅ Mᴀʀsʜᴇʟゞメ🇮🇳</a>"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
