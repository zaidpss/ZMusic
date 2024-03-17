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
  command(["مطور","المطور"])
)
async def huhh(client: Client, message: Message):
    # افتراضياً، لنفترض أن "us_id" هو ايدي المستخدم للمطور
    us_id = "123456789"  # استبدل بالقيمة الفعلية لايدي المطور

    # احصل على معلومات المطور باستخدام الايدي المحدد
    # يمكنك استبدال الطريقة التي تحصل بها على معلومات المطور بوظيفة أخرى
    developer_info = await client.get_users(us_id)

    await message.reply_photo(
        photo=developer_info.photo.big_file_id,
        caption=f"""<b>⌯ المطور :</b> <a href="tg://user?id={us_id}">{developer_info.first_name}</a>
        
<b>⌯ معرف المطور :</b> @{developer_info.username}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/{developer_info.username}"), 
                 ],
            ]

        ),

    )
