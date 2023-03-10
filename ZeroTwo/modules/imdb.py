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
ð á´Éªá´Êá´ : {title}

â±ï¸ Êá´É´á´Éªá´á´ : {runtime}á´ÉªÉ´
ð Êá´á´ÉªÉ´É¢ : {rating}/10
ð³ï¸ Éªá´ : {id}

ð Êá´Êá´á´sá´ á´á´á´á´ : {releaseDate}
ð­ É¢á´É´Êá´ : {genres}
ð¥ á´á´á´á´Êá´ÊÉªá´Ê : {popularity}

â¡ sá´á´á´á´s : {status}
ð« Éªá´á´Ê Éªá´ : {imdbId}

ð  á´Êá´á´ : {overview}
""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ðï¸ ð¸ð¼ð³Ê",
                        url=imdbLink,
                    ),
                ],
            ],
        ),
    )


__help__ = """
 â /imdb <Movie name>*:* Get full info about a movie from [imdb.com](https://m.imdb.com)
"""

__mod_name__ = "ð¸á´á´Ê"
