import logging
import os
import random
import conf


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
        fr'{user.mention_markdown_v2()}{conf.GREETING}'
    )

    chat_id = update.message.chat_id
    send_image(chat_id,update,context)


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('you can get help visiting https://github.com/diesilveira/labeller_img_python_telegram_BOT ')


def get_image():
    if conf.LOCAL:
        img_id = random.choice(os.listdir(conf.PATH_FOLDER))
        with open('finished.txt', 'r') as f:
            finished = f.readlines()
        while img_id in finished:
            img_id = random.choice(os.listdir(conf.PATH_FOLDER))

        image = os.path.join(conf.PATH_FOLDER, img_id)

    else:
        with open('url_images.txt', 'r') as f:
            lines = f.readlines()
        image = random.choice(lines)
        img_id = image.split(';')[0]
        with open('finished.txt', 'r') as f:
            finished = f.readlines()
        while img_id in finished:
            image = random.choice(lines)
            img_id = image.split(';')[0]

    return [image, img_id]


def generate_keyboard(img_id):
    keyboard = []
    i = 0
    if len(conf.BUTTONS) % 2 == 1:
        keyboard.append([InlineKeyboardButton(conf.BUTTONS[i], callback_data=img_id + ',' + conf.BUTTONS[i])])
        i = i + 1
    for x in range(len(conf.BUTTONS) // 2):
        keyboard.append([InlineKeyboardButton(conf.BUTTONS[i], callback_data=img_id + ',' + conf.BUTTONS[i]),
                         InlineKeyboardButton(conf.BUTTONS[i + 1], callback_data=img_id + ',' + conf.BUTTONS[i + 1])])
        i += 2
    return keyboard

def send_image(chat_id, update: Update, context: CallbackContext) -> None:
    """send image to tag."""
    image_path_and_id = get_image()
    image = image_path_and_id[0]
    img_id = image_path_and_id[1]

    if conf.LOCAL:
        with open(image, 'rb') as f:
            context.bot.send_photo(chat_id, photo=f)
    else:
        context.bot.send_photo(chat_id, photo=image.split(';')[1])

    keyboard = generate_keyboard(img_id)
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id, text= conf.QUESTION , reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.answer():
        query.edit_message_text(text=f"{conf.CHOSE} {query.data.split(',')[1]}")

    chat_id = update.callback_query.message.chat.id

    with open("log.txt", 'a') as f:
        f.write(query.data + '\n')

    with open('finished.txt', 'a') as f:
        f.write(query.data.split(',')[0] + '\n')

    send_image(chat_id, update, context)
