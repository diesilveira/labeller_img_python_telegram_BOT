import logging
import utils
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


class Bot:

    def __init__(self):
        self.last_msg = None
        self.hist = {}

    def set_last_msg(self, msg_id):
        self.last_msg = msg_id

    def get_last_msg(self):
        return self.last_msg

    def set_last_msg_for_chat_id(self, chat_id, msg_id):
        self.hist.update({chat_id: [msg_id]})

    def get_last_msg_for_chat_id(self, chat_id):
        return self.hist[chat_id][-1]

    def get_msg_list_for_chat_id(self, chat_id) -> list:
        return self.hist[chat_id]

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        """
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'{user.mention_markdown_v2()}{conf.GREETING}'
        )
        """
        chat_id = update.message.chat_id
        msg_id = update.message.message_id

        image = utils.get_random_image()

        self.set_last_msg_for_chat_id(chat_id, msg_id)
        self.set_last_msg(msg_id)
        self.send_image(chat_id, image, update, context)

    def help_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            'you can get help visiting https://github.com/diesilveira/labeller_img_python_telegram_BOT ')

    def send_image(self, chat_id, image, update: Update, context: CallbackContext) -> None:
        """send image to tag."""
        keyboard = utils.generate_keyboard(image[1], chat_id)
        reply_markup = InlineKeyboardMarkup(keyboard)

        if conf.LOCAL:
            with open(image[0], 'rb') as f:
                context.bot.send_photo(chat_id, photo=f, reply_markup=reply_markup, disable_notification=True)
                msg_list = self.get_msg_list_for_chat_id(chat_id)
                msg_list.append(msg_list[-1] + 1)

        else:
            print(image)
            context.bot.send_photo(chat_id, photo= image[0], reply_markup=reply_markup, disable_notification=True)
            msg_list = self.get_msg_list_for_chat_id(chat_id)
            msg_list.append(msg_list[-1] + 1)
            self.hist.update({chat_id: msg_list})

    def button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        chat_id = update.callback_query.message.chat.id

        if utils.get_action_query_data(query) == conf.UNDO:
            utils.get_rid_of_this_img(utils.get_action_result_query_data(query))

            keyboard = [[InlineKeyboardButton(conf.SUCCES_UNDO, callback_data="-")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_reply_markup(reply_markup=reply_markup)

        elif utils.get_action_query_data(query) == '-':
            return
        else:
            if query.answer():
                reply_markup = InlineKeyboardMarkup(utils.generate_undo_keyboard(query))
                query.edit_message_reply_markup(reply_markup=reply_markup)

            with open("log.txt", 'a') as f:
                f.write(query.data + '\n')

            with open('finished.txt', 'a') as f:
                f.write(query.data.split(',')[0] + '\n')

            user = update.effective_user
            with open('log_users.txt', 'a') as f:
                f.write(fr'{user.mention_markdown_v2()}' + '\n')

            image = utils.get_random_image()
            self.send_image(chat_id, image, update, context)

            if len(self.get_msg_list_for_chat_id(chat_id)) > 10:
                list_msgs = self.get_msg_list_for_chat_id(chat_id)
                for i in range(9):
                    context.bot.delete_message(chat_id=chat_id, message_id=list_msgs[0])
                    list_msgs.pop(0)
                self.hist.update({chat_id: list_msgs})
