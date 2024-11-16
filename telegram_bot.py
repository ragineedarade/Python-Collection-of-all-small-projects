import telegram.ext

token = "6468250054:AAHVZHvvil19ZiOobdOmKr0JU-ZTUZoBoFQ"
updater = telegram.ext.updater(token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("Hello, Welcome")


def help(update, context):
    update.message.reply_text("""
        /start -> welcome to the channel
        /help -> this particular message
        /content -> about various playlist
        /portfolio -> about my portfolio
        /career -> about career life 
    """)


def content(update, context):
    update.message.reply_text("We have many functions and playlists.")


def portfolio(update, context):
    update.message.reply_text(
        "Portfolio link: https://sites.google.com/view/ragineedarade/home")


def career(update, context):
    update.message.reply_text("My YouTube link: https://www.youtube.com/channel/UC3_fYtmeGo51dcImvqsW6cw\n"
                              "My LinkedIn link:  https://www.linkedin.com/in/raginee-darade/")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
dispatcher.add_handler(telegram.ext.CommandHandler('portfolio', portfolio))
dispatcher.add_handler(telegram.ext.CommandHandler('career', career))
updater.start_polling()
updater.idle()
