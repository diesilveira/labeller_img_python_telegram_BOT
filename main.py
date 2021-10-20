import telegram

import labellerBot
import conf

def main() -> None:
    """Start the bot."""
    updater = labellerBot.Updater(conf.TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(labellerBot.CommandHandler("start", labellerBot.start))
    dispatcher.add_handler(labellerBot.CommandHandler("help", labellerBot.help_command))
    dispatcher.add_handler(labellerBot.CommandHandler("image", labellerBot.send_image))

    updater.dispatcher.add_handler(labellerBot.CallbackQueryHandler(labellerBot.button))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
