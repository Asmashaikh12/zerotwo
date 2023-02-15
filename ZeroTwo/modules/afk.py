"""
MIT License

Copyright (c) 2022 Arsh

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

from typing import Optional
import time
import random

from telegram import Message, User
from telegram import MessageEntity, ParseMode
from telegram.error import BadRequest
from telegram.ext import Filters, MessageHandler

from ZeroTwo import dispatcher
from ZeroTwo.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from ZeroTwo.modules.redis.afk_redis import start_afk, end_afk, is_user_afk, afk_reason
from ZeroTwo import REDIS
from ZeroTwo.modules.users import get_user_id

from ZeroTwo.modules.helper_funcs.alternate import send_message
from ZeroTwo.modules.helper_funcs.readable_time import get_readable_time

AFK_GROUP = 7
AFK_REPLY_GROUP = 8

def afk(update, context):
    args = update.effective_message.text.split(None, 1)
    user = update.effective_user
    if not user:  # ignore channels
        return

    if user.id == 777000:
        return
    start_afk_time = time.time()
    if len(args) >= 2:
        reason = args[1]
    else:
        reason = "none"
    start_afk(update.effective_user.id, reason)
    REDIS.set(f'afk_time_{update.effective_user.id}', start_afk_time)
    fname = update.effective_user.first_name
    random_afk_msg = (
        "Naruhodo! Watching porn again?",
        "Yeah sleep already.",
        "Haah! Maybe doing something lewd behind my back.",
        "Okay, updating your afk status, be grateful to me.",
        "I know you are reading..... May be Doujins",
        "So, you finally decided to leave. Maybe going to relieve your stress in form of your fluids.",
        "I don't think you got a girl that you are ignoring this precious chat, so what are you upto?",
        "Wakatta! Sayonara👋",
        "Okay! Have you decided to do something useful or still jerking off?",
        "Damn! You're leaving, like I will even miss you.",
        "Yeah leave! Group feels so clean now.",
        "See ya! Now I'll enjoy my observations here.",
        "I was about to ask you for a coffee, but you are leaving already.",
        "Yes! Go away, you are a troublesome.😏",
        "Don't you wanna hear my wuv story🥰..",
        "Hmmph! Leave already.\n*angry cute pouts*",
        "Wtf, going already? Not like I care about it.",
        "Do you know what it feels like in lava? Just go and sink in it 🔥",
        "Bye bye!!! Cum back soon",
        'Before leaving, He told me "Be the tsun to my dere". Such a lewd brat',
        "Enjoy fapping.. I mean napping*.",
        "Stop dreaming that you'll find a date.",
        "A Snowball fight? No thanks! You might hit me on my chest.",
        "I think there is no Girl in this chat, that's why you are going away.",
        "*Don't tell my Maestro about this*, if you'll wait I can flirt with you a little.",
        "Do you know anything about a Thigh massage Job? Oops my bad, I meant Thai* Massage Jobs.",
        "Mind if I come along with you? Only if you are not thinking something lewd.",
        "A steamy bath, I am back without a Towel. Thank God you are leaving, perv.",
        "Hmmmmmmmm. Wanking off?",
        "Did you just shot some sticky stuff on your phone by seeing my pic? That's why going away.",
        "Fine! I won't be a bother, like I care if you are away. Hmmphh",
        "You playing CS:GO now? My kill streak is 13, but I don't play any games.🔪🪓🩸",
        "Yeah, Go away Horny.",
    )
    afk_msg = random.choice(random_afk_msg)
    try:
        update.effective_message.reply_text(
            "{} is now away!\n{}".format(fname, afk_msg)
        )
    except BadRequest:
        pass

def no_longer_afk(update, context):
    user = update.effective_user
    message = update.effective_message
    if not user:  # ignore channels
        return

    if not is_user_afk(user.id):  #Check if user is afk or not
        return
    end_afk_time = get_readable_time((time.time() - float(REDIS.get(f'afk_time_{user.id}'))))
    REDIS.delete(f'afk_time_{user.id}')
    res = end_afk(user.id)
    if res:
        if message.new_chat_members:  #dont say msg
            return
        firstname = update.effective_user.first_name
        try:
            options = [
                "{} arrived! I saw you were stocking in this chat! aren't you? and was away for {}",
                "Hehe, {} is back now, how tf you were even busy? and btw you were away for {}",
                "Guys, {} got a girlfried, that's why he was busy for {}.",
                "{}, chotto matte!! you came out of no where! and you were away for {}",
                "{}, Spammer D2 arrived, lemme grab my ban hammer and was away for {}.",
                "{}, go back to sleep!!! and was away for {}",
                "The Dead {} Came Back From His Grave! Time Taken: {}",
                "Hey {} Darling, Welcome Back! We Were Apart For {}",
                "{} Came Back After Masturbating! Time Taken: {}",
                "OwO, Welcome Back {}! You Were Missing Since {} ",
                "Were you playing Poker, {}? A Strip Poker, hehe!!!\n and you were gone for {}",
                "Yeah, pro like {} arrived again, beware of some noobs!!!\n and was away for {}",
                "Dear {}, Are you a BTS Lover. I know you were watching it? and was away for {}",
                "{}, I know were watching something dirty, that's why you were gone for {}",
                "Why came back, {}? Girls are away from chat already, btw you were gone for {}.",
                "{} bas wapas ja.",
                "{}, Irrashaimase!",
                "Horny user '{}' is back and was away for {}",
                "{}-San, you are back for me, aren't you? and was away for {}",
                "{}, I know what you were doing.😏✊.\nAnyway, welcome back and you were apart for {}",
                "Okairinasai {} Nii-Chan!! ayou were way for {}",
                "Where is {}?\nIn the chat! and was away for {}",
                "{}, were you doing something lewd?\nI just saw a white stain on your T-shirt btw you were away for {}.",
            ]
            chosen_option = random.choice(options)
            update.effective_message.reply_text(
                chosen_option.format(firstname, end_afk_time),
            )
        except BaseException:
            pass


def reply_afk(update, context):
    message = update.effective_message
    userc = update.effective_user
    userc_id = userc.id
    if message.entities and message.parse_entities(
        [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]):
        entities = message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION])

        chk_users = []
        for ent in entities:
            if ent.type == MessageEntity.TEXT_MENTION:
                user_id = ent.user.id
                fst_name = ent.user.first_name

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

            elif ent.type == MessageEntity.MENTION:
                user_id = get_user_id(message.text[ent.offset:ent.offset +
                                                   ent.length])
                if not user_id:
                    # Should never happen, since for a user to become AFK they must have spoken. Maybe changed username?
                    return

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

                try:
                    chat = context.bot.get_chat(user_id)
                except BadRequest:
                    print("Error: Could not fetch userid {} for AFK module".
                          format(user_id))
                    return
                fst_name = chat.first_name

            else:
                return

            check_afk(update, context, user_id, fst_name, userc_id)

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fst_name = message.reply_to_message.from_user.first_name
        check_afk(update, context, user_id, fst_name, userc_id)


def check_afk(update, context, user_id, fst_name, userc_id):
    if is_user_afk(user_id):
        reason = afk_reason(user_id)
        since_afk = get_readable_time((time.time() - float(REDIS.get(f'afk_time_{user_id}'))))
        if reason == "none":
            if int(userc_id) == int(user_id):
                return
            LEVI = [
                "Is With Your GF!",
                "Is With Your BF!",
                "Is Masturbating! Please Don't Disturb Him.",
                "Is With Your Crush",
                "Is With Your Sis",
                "Is Playing Squid Game, He Will Come Back After Winning A Lot Of Money🤑",
            ]
            LEVII = random.choice(LEVI)
            res = "{} {}\n⏱️ Last seen {} ago.".format(fst_name, LEVII, since_afk)
            update.effective_message.reply_text(res)
        else:
            if int(userc_id) == int(user_id):
                return
            res = "{} is afk.\nReason: {}\n⏱️ Last seen {} ago.".format(fst_name, reason, since_afk)
            update.effective_message.reply_text(res)


def __user_info__(user_id):
    is_afk = is_user_afk(user_id)
    text = ""
    if is_afk:
        since_afk = get_readable_time((time.time() - float(REDIS.get(f'afk_time_{user_id}'))))
        text = "<i>This user is currently afk (away from keyboard).</i>"
        text += f"\n<i>Since: {since_afk}</i>"
       
    else:
        text = "<i>This user is currently isn't afk (away from keyboard).</i>"
    return text


def __gdpr__(user_id):
    end_afk(user_id)



__mod_name__ = "𝙰ғᴋ"


AFK_HANDLER = DisableAbleCommandHandler("afk", afk)
AFK_REGEX_HANDLER = MessageHandler(Filters.regex("(?i)brb"), afk)
NO_AFK_HANDLER = MessageHandler(Filters.all & Filters.group, no_longer_afk)
AFK_REPLY_HANDLER = MessageHandler(Filters.all & Filters.group, reply_afk)

dispatcher.add_handler(AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REGEX_HANDLER, AFK_GROUP)
dispatcher.add_handler(NO_AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REPLY_HANDLER, AFK_REPLY_GROUP)
