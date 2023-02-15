"""
MIT License

Copyright (c) 2022 Aʙɪsʜɴᴏɪ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import html
import asyncio
import random
from sys import version_info
import datetime
from datetime import datetime

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telegram import update
from telethon import __version__ as tver

from ZeroTwo import BOT_NAME
from ZeroTwo import OWNER_USERNAME, SUPPORT_CHAT, pgram

PHOTO = ["https://telegra.ph/file/b986186c33538625a1e2e.mp4"]

ASAU = [
    [
        InlineKeyboardButton(text="🚑Support", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
]

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@pgram.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ ʙᴀʙʏ ....")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker(
        "CAACAgUAAx0CaYJXkAACDfhjPVg7KWbBT2g44lRtiN24JpzNaQACcwcAAiRO8VXjkW9AnnwsLSoE"
    )
    await asyncio.sleep(0.1)
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_video(
        random.choice(PHOTO),
        caption=f"""<b>✨I'm Alive Baby\n🥀I'm Working Perfectly</b>
     ▱▱▱▱▱▱▱▱▱▱▱▱
🔱<b>My Owner:</b> <a href="https://t.me/HssLevii">𝒍𝒆𝒗𝒊</a>
🐍<b>Library Version:</b> <code>{lver}</code>
🤖<b>Bot Version: 2.0</b>
⚡️<b>My Uptime:</b> <code>{uptime}</code>
     ▱▱▱▱▱▱▱▱▱▱▱▱""",
        reply_markup=InlineKeyboardMarkup(ASAU),
    )
