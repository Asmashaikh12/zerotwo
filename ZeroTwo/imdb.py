import requests
from ZeroTwo import pgram as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("imdb"))
async def IMDb(_,msg):
    if len(msg.command) < 2:        
        await msg.reply_text("give me a query to search")
    else:
        pass 
    text = (
        msg.text.split(None, 1)[1]
        if len(msg.command) < 3
        else msg.text.split(None, 1)[1].replace(" ", "%20")
    )
    url=f"https://api.safone.me/tmdb?query={text}%20&limit=1"
    re=requests.get(url).json()["results"][0]
    title=re["title"]
    poster=re["poster"]
    runtime=re["runtime"]
    rating=re["rating"]
    releaseDate=re["releaseDate"]
    genres=re["genres"][0:]
    popularity=re["popularity"]
    status=re["status"]
    homepage=re["homepage"]
    imdbId=re["imdbId"]
    imdbLink=re["imdbLink"]
    id=re["id"]        
    overview=re["overview"]        
    await msg.reply_photo(poster,
    caption=f"""
📀 ᴛɪᴛʟᴇ : {title}

⏱️ ʀᴜɴᴛɪᴍᴇ : {runtime}ᴍɪɴ
🌟 ʀᴀᴛɪɴɢ : {rating}/10
🗳️ ɪᴅ : {id}

📆 ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ : {releaseDate}
🎭 ɢᴇɴʀᴇ : {genres}
🥂 ᴘᴏᴘᴜʟᴀʀɪᴛʏ : {popularity}

⚡ sᴛᴀᴛᴜs : {status}
🎫 ɪᴍᴅʙ ɪᴅ : {imdbId}

🗒  ᴘʟᴏᴛ : {overview}
""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🎟️ 𝙸𝙼𝙳ʙ",
                        url=imdbLink,
                    ),
                ],
            ],
        ),
    )


__help__ = """
 ❍ /imdb <Movie name>*:* Get full info about a movie from [imdb.com](https://m.imdb.com)
"""

__mod_name__ = "𝙸ᴍᴅʙ"
