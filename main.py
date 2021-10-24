import conf
from bot import *


def main() -> None:
    """Start the bot."""
    # Enable logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    bot = Bot()
    updater = Updater(conf.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("help", bot.help_command))

    updater.dispatcher.add_handler(CallbackQueryHandler(bot.button))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
