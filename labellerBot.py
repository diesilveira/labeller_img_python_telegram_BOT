import logging
import os
import random
import conf
from threading import *

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup)

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hello {user.mention_markdown_v2()}\!, send me the word "/image"'
    )


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('you can get help visiting https://github.com/diesilveira/labeller_img_python_telegram_BOT')


def send_image(update: Update, context: CallbackContext) -> None:
    """send image to tag."""
    img = random.choice(os.listdir(conf.PATH_FOLDER))
    semaphore = Semaphore(1)
    semaphore.acquire()
    with open('finished.txt', 'r') as f:
        finished = f.readlines()
    while img in finished:
        img = random.choice(os.listdir(conf.PATH_FOLDER))

    image = os.path.join(conf.PATH_FOLDER, img)
    with open(image, 'rb') as f:
        update.message.reply_photo(photo=f)
    semaphore.release()

    keyboard = []
    i = 0
    if len(conf.buttons) % 2 == 1:
        keyboard.append([InlineKeyboardButton(conf.buttons[i], callback_data=img + ',' + conf.buttons[i])])
        i = i + 1
    for x in range(len(conf.buttons) // 2):
        keyboard.append([InlineKeyboardButton(conf.buttons[i], callback_data=img + ',' + conf.buttons[i]),
                         InlineKeyboardButton(conf.buttons[i + 1], callback_data=img + ',' + conf.buttons[i + 1])])
        i += 2

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(conf.question, reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Chose: {query.data.split(',')[1]}")
    semaphore = Semaphore(1)
    semaphore.acquire()
    with open("log.txt", 'a') as f:
        f.write(query.data + '\n')

    with open('finished.txt', 'a') as f:
        f.write(query.data.split(',')[0] + '\n')
    semaphore.release()
