import asyncio
import os
import time
import requests
import aiohttp
from strings.filters import command
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(filters.command(["مالك"]))
async def show_owner_info(client, message):
    # الحصول على قائمة الإداريين للمجموعة
    chat_id = message.chat.id
    admins = await client.get_chat_members(chat_id, filter="administrators")

    # البحث عن المالك بين قائمة الإداريين
    for admin in admins:
        if admin.status == "creator":
            owner_id = admin.user.id
            owner_info = await client.get_users(owner_id)

            # إعداد الرد مع معلومات المالك
            owner_text = f"👑 **معلومات المالك** 👑\n\n"
            owner_text += f"اسم المالك: [{owner_info.first_name}](tg://user?id={owner_id})\n"
            owner_text += f"معرف المالك: @{owner_info.username}\n"
            owner_text += f"معرف المجموعة: {message.chat.title}"

            # إرسال الرد
            await message.reply_text(owner_text, parse_mode="markdown")
            return

    # إرسال رسالة في حالة عدم العثور على المالك
    await message.reply_text("لا يمكن العثور على معلومات المالك في هذه المجموعة.")

   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""") 

        

array = []
@app.on_message(command(["@all", "تاك","تاك للكل"]) & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("**التاك قيد التشغيل حالياً ،**")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🖱️**")
    return
  await message.reply_text("**جاري بدأ المنشن ، لايقاف الامر اضغط **\n /cancel او اكتب بس منشن")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("نادي الكل","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.iter_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 5:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(command(["بس المنشن", "/cancel","بس منشن"]))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🖱️")
    return
  if message.chat.id not in array:
     await message.reply("**المنشن متوقف بالفعل**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("**تم ايقاف المنشن بنجاح✅**")
    return




