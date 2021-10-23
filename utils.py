import conf
import os
import random
from telegram import InlineKeyboardButton

def get_random_image():
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
        image = random.choice(lines).split(';')[1]
        img_id = image.split(';')[0]
        with open('finished.txt', 'r') as f:
            finished = f.readlines()
        while img_id in finished:
            image = random.choice(lines).split(';')[1]
            img_id = image.split(';')[0]

    return [image, img_id]

def get_this_image(img_id):
    if conf.LOCAL:
        image = os.path.join(conf.PATH_FOLDER, img_id)

    else:
        with open('url_images.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.split(';')[0] == img_id:
                    image = line.split(';')[1]

    return [image, img_id]


def generate_keyboard(img_id, chat_id):
    keyboard = []
    i = 0
    if len(conf.BUTTONS) % 2 == 1:
        keyboard.append([InlineKeyboardButton(conf.BUTTONS[i],
                                              callback_data=img_id + ',' + conf.BUTTONS[i])])
        i = i + 1
    for x in range(len(conf.BUTTONS) // 2):
        keyboard.append([InlineKeyboardButton(conf.BUTTONS[i],
                                              callback_data=img_id + ',' + conf.BUTTONS[i]),
                         InlineKeyboardButton(conf.BUTTONS[i + 1],
                                              callback_data=img_id + ',' + conf.BUTTONS[i + 1])])
        i += 2
    return keyboard