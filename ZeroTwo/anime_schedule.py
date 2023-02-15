from pyrogram import filters
import requests
from ZeroTwo import pgram as pbot
from pytz import timezone
from datetime import datetime
from pyrogram.enums import ParseMode

def get_indian_tz_time(hour, minutes):
    current_time = datetime.now()
    date_converted = datetime(current_time.year, current_time.month, current_time.day, int(hour), int(minutes),
                              tzinfo=timezone("Japan")).astimezone(timezone("Asia/Kolkata"))
    return date_converted.strftime("%I:%M %p")


@pbot.on_message(filters.command('latest'))
@pbot.on_message(filters.command('schedule'))
def schedule(_, message):
    results = requests.get('https://subsplease.org/api/?f=schedule&h=true&tz=Japan').json()
    text = None
    for result in results['schedule']:
        title = result['title']
        hours, minutes = result['time'].split(':')
        time = get_indian_tz_time(hours, minutes)
        aired = bool(result['aired'])
        title = f"**[{title}](https://subsplease.org/shows/{result['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{result['page']})~~**"
        data = f"{title} - **{time}**"

        if text:
            text = f"{text}\n{data}"
        else:
            text = data

    message.reply_text(f"**Today's Schedule:**\nTime-Zone: Indian (GMT +9)\n\n{text}", parse_mode=ParseMode.MARKDOWN)


__mod_name__ = "𝙰ɴɪᴍᴇ 𝚂ᴄʜᴇᴅᴜʟᴇ"

__help__ = """
 ❍ `/latest` or `/schedule`: to see latest anime episodes schedule time in IST (Indian Standard Time) Zone.
Note: You can use this command only in groups.
"""
