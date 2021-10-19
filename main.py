import labellerBot
import conf
import os
PORT = int(os.environ.get('PORT', 5000))

def main() -> None:
    """Start the bot."""
    updater = labellerBot.Updater(conf.TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(labellerBot.CommandHandler("start", labellerBot.start))
    dispatcher.add_handler(labellerBot.CommandHandler("help", labellerBot.help_command))
    dispatcher.add_handler(labellerBot.CommandHandler("image", labellerBot.send_image))

    updater.dispatcher.add_handler(labellerBot.CallbackQueryHandler(labellerBot.button))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=conf.TOKEN)
    updater.bot.setWebhook('https://gentle-wave-49183.herokuapp.com/' + conf.TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
