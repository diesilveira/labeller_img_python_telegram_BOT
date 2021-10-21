import labeller_bot
import conf

def main() -> None:
    """Start the bot."""
    updater = labeller_bot.Updater(conf.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(labeller_bot.CommandHandler("start", labeller_bot.start))
    dispatcher.add_handler(labeller_bot.CommandHandler("help", labeller_bot.help_command))

    updater.dispatcher.add_handler(labeller_bot.CallbackQueryHandler(labeller_bot.button))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
