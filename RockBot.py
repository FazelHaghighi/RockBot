from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

TOKEN = "You will never know my token!"

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Wow, new user! I'm here to don't give a shit about your problems.\n\nType /help to see the allowed commands, you idiot!")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/start - start bot\n/info - send the bot creator's info\n")

def info_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Linkedin: https://www.linkedin.com/in/mohammadfazel-abdhaghighi-33912a234\n\nGitHub: https://github.com/FazelHaghighi")

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "'%s' is not even a command you dumb cunt!" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "WTF man? Are you a fuckin dumb? I told you what commands I understand. What the fuck is '%s' ?" % update.message.text)

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('info', info_url))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))
dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
