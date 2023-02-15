from typing import Optional, List
from gtts import gTTS
import os
import requests
import json

from telegram import ChatAction
from telegram.ext import run_async

from ZeroTwo import dispatcher
from ZeroTwo.modules.disable import DisableAbleCommandHandler
from ZeroTwo.modules.helper_funcs.alternate import send_action

@send_action(ChatAction.RECORD_AUDIO)
def gtts(update, context):
    msg = update.effective_message
    reply = " ".join(context.args)
    if not reply:
        if msg.reply_to_message:
            reply = msg.reply_to_message.text
        else:
            return msg.reply_text(
                "Reply to some message or enter some text to convert it into audio format!"
            )
        for x in "\n":
            reply = reply.replace(x, "")
    try:
        tts = gTTS(reply, lang='en', tld='co.in')
        tts.save("k.mp3")
        with open("k.mp3", "rb") as speech:
            msg.reply_audio(speech)
    finally:
        if os.path.isfile("k.mp3"):
            os.remove("k.mp3")


# Open API key
API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


dispatcher.add_handler(DisableAbleCommandHandler("tts", gtts, pass_args=True, run_async=True))

__help__ = """
 ‣ `/tts`: Convert Text in Bot Audio 
 *Usage*: reply to text or write message with command. Example `/tts hello`
"""
__mod_name__ = "𝚃ᴇxᴛ 𝚃ᴏ 𝚂ᴘᴇᴇᴄʜ"
__command_list__ = ["tts"]
