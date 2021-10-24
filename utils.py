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
        get_image = random.choice(lines).split(';')
        image = get_image[1]
        img_id = get_image[0]
        with open('finished.txt', 'r') as f:
            finished = f.readlines()
        while img_id in finished:
            get_image = random.choice(lines).split(';')
            image = get_image[1]
            img_id = get_image[0]

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

def generate_undo_keyboard(query):
    keyboard = [[InlineKeyboardButton(f"{conf.CHOSE} {get_action_result_query_data(query)} ¿{conf.UNDO}?",
                                      callback_data=conf.UNDO + ',' + get_action_query_data(query))]]
    return keyboard

def get_rid_of_this_img(img_id):
    with open("log.txt", "r") as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if line.split(',')[1] == img_id:
            pass
        else:
            new_lines.append(line)
    with open("log.txt", "w") as f:
        f.writelines(new_lines)
    with open("finished.txt", "r") as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if line == img_id:
            pass
        else:
            new_lines.append(line)
    with open("finished.txt", "w") as f:
        f.writelines(new_lines)


def get_action_query_data(query):
    return query.data.split(',')[0]


def get_action_result_query_data(query):
    return query.data.split(',')[1]