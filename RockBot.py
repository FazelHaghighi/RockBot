from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("You will never know my token!",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Wow, new user! I'm here to don't give shit about your problems.\n\nType /help to see the allowed commands you idiot!")


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/start - start bot\n/info - send the bot maker's info\n")


def info_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Linkedin: https://www.linkedin.com/in/mohammadfazel-abdhaghighi-33912a234\n\nGitHub: https://github.com/FazelHaghighi")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "'%s' is not even a command you dumb cunt!" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "WTF man? Are you a fuckin dumb? I told you what commands I understand. What the fuck is '%s' ?" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('info', info_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
