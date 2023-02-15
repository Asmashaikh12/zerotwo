from pyrogram import Client, filters
from pyrogram.types import Message

from ZeroTwo import OWNER_ID
from ZeroTwo import pgram as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if message.from_user.id != 5667156680:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
