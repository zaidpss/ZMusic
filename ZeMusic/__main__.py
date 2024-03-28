import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ZeMusic import LOGGER, app, userbot
from ZeMusic.core.call import Mody
from ZeMusic.misc import sudo
from ZeMusic.plugins import ALL_MODULES
from ZeMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ZeMusic.plugins" + all_module)
    LOGGER("ZeMusic.plugins").info("تنزيل معلومات السورس...")
    await userbot.start()
    await Mody.start()
    try:
        await Mody.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ZeMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Mody.decorators()
    LOGGER("ZeMusic").info(
        "\xd8\xac\xd8\xa7\xd8\xb1\xd9\x8a \xd8\xaa\xd8\xb4\xd8\xba\xd9\x8a\xd9\x84 \xd8\xa7\xd9\x84\xd8\xa8\xd9\x88\xd8\xaa\n\n\xd8\xaa\xd9\x85 \xd8\xaa\xd9\x86\xd8\xb5\xd9\x8a\xd8\xa8 \xd8\xb3\xd9\x88\xd8\xb1\xd8\xb3 \xd8\xa7\xd9\x84\xd9\x85\xd9\x84\xd9\x83 \xd8\xa8\xd9\x86\xd8\xac\xd8\xa7\xd8\xad\n\n\xd9\x82\xd9\x86\xd8\xa7\xd8\xa9 \xd8\xa7\xd9\x84\xd8\xb3\xd9\x88\xd8\xb1\xd8\xb3 https://t.me/EF_19"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    await azkar()
    LOGGER("ZeMusic").info("Stopping Ze Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
