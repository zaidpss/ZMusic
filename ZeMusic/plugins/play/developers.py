import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(
  command(["مطور","مطور السورس","مبرمج السورس","المطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1a77a02bdb06d55051845.jpg",
        caption=f"""<b>⌯ 𝙽𝙰𝙼𝙴 :</b> <a href="https://t.me/IC_19">『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』</a>
        
<b>⌯ 𝙱𝙸𝙾  :</b> ـ ی‍‌ت‍‌ع‍‌افی ال‍‌م‍‌رء ب‍‌ال‍‌له ف‍‌ق‍‌ط‍‌ >ᯓ𓆰᭼١9""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『 🇾🇪⃤𝐀𝐁𝐃𝐔𝐋𝐋𝐀𝐇 个 ١9 』", url=f"https://t.me/IC_19"), 
                 ],[
                   InlineKeyboardButton(
                        "『 𝙺𝙸𝙽𝙶 𝚂𝙾𝚄𝚁𝙲𝙴 』", url=f"https://t.me/EF_19"),
                ],

            ]

        ),

    )
