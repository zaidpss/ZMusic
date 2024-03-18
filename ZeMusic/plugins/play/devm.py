import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["مطور", "", "المطور"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>⌯ 𝙽𝙰𝙼𝙴 :</b> <a href="https://t.me/{usrnam}">{name}</a>

<b>⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :</b> @{usrnam}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "•✯  السورس  ✯•", url="https://t.me/EF_19"),
                ],
            ]
        ),
    )
