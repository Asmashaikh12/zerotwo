import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import ZeroTwo.modules.game_strings as game_strings
from ZeroTwo import dispatcher
from ZeroTwo.modules.disable import DisableAbleCommandHandler
from ZeroTwo.modules.helper_funcs.chat_status import (is_user_admin)
from ZeroTwo.modules.helper_funcs.extraction import extract_user


@run_async
def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.TRUTH_STRINGS))


@run_async
def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.DARE_STRINGS))


@run_async
def tord(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.TORD_STRINGS))

@run_async
def sex(update: Update, context: CallbackContext):
    reply_animation = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_animation(random.choice(game_strings.SEX))

@run_async
def wyr(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.WYR_STRINGS))


__help__ = """
 • `/truth`*:* asks you a question
 • `/dare`*:* gives you a dare
 • `/TorD`*:* can be a truth or a dare
 • `/rather`*:* would you rather
  """

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord)
WYR_HANDLER = DisableAbleCommandHandler("rather", wyr)
SEX_HANDLER = DisableAbleCommandHandler("sex", sex)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(TORD_HANDLER)
dispatcher.add_handler(WYR_HANDLER)
dispatcher.add_handler(SEX_HANDLER)

__mod_name__ = "𝙶ᴀᴍᴇs"
__command_list__ = [
   "truth", "dare", "tord", "sex" "rather",
]

__handlers__ = [
    TRUTH_HANDLER, DARE_HANDLER, TORD_HANDLER, SEX_HANDLER, WYR_HANDLER,
]
