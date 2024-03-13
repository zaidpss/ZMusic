# This code is written by (C) TheTeamAlexa bot will send message to log group when someone add
# this bot to new group make sure to star all projects
# Copyright (C) 2021-2022 by Alexa_Help@ Github, < TheTeamAlexa >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki

from pyrogram import Client, filters
from pyrogram.types import Message
from ZeMusic import app
from ZeMusic.utils.database import get_served_chats
from config import LOGGER_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "مستخدم غير معروف"
        added_id = message.from_user.id

        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"🌹 ʙᴏᴛ ᴀᴅᴅᴇᴅ ᴛᴏ ɴᴇᴡ ɢʀᴏᴜᴘ ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ <b>ᴄʜᴀᴛ</b> › :<a href='tg://user?id={chat_id}'> {matlabi_jhanto}</a>\n┣★ <b>ᴄʜᴀᴛ ɪᴅ</b> › : {chat_id}\n┣★ <b>ᴄʜᴀᴛ ᴜɴᴀᴍᴇ</b> › : {chatusername}\n┣★ <b>ᴛᴏᴛᴀʟ ᴄʜᴀᴛ</b> › : {served_chats}\n┣★ <b>ᴀᴅᴅᴇᴅ ʙʏ</b> › :\n┗━━━ <a href='tg://user?id={added_id}'>{added_by}</a>"
        await lul_message(LOGGER_ID, lemda_text)
