import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from config import OWNER_ID

@app.on_message(filters.command("بوت", prefixes=""))
async def ZeMusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الى مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 5145609515:
             rank = "\n<b>⌯ رتبتك هي : مطور الس‍‌ورس 🫶🏻.</b>"
        elif user_id == OWNER_ID:
             rank = "\n<b>⌯ رتبتك هي : مـالك الـبوت 🫡.</b>"
        else:
             rank = ""
    except Exception as e:
        print(e)
        rank = ""

    await message.reply_text(f"<b>⌯ نعم حبيبي :</b> {italy}\n<b>⌯ انا اسمي القميل :</b> {bot_name} 🥺🙈 {rank}", reply_markup=keyboard)
