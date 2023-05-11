from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "You will never know my token!"

def start(update: Update, context):
    message = "Wow, new user!\nI'm here to don't give a shit about your problems.\nType /help to see the available commands."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def help(update: Update, context):
    message = "/start - Start the bot\n/info - Get the bot creator's information"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def info_url(update: Update, context):
    linkedin_text = "LinkedIn Profile"
    linkedin_link = "https://www.linkedin.com/in/mohammadfazel-abdhaghighi-33912a234"
    
    github_text = "GitHub Profile"
    github_link = "https://github.com/FazelHaghighi"
    
    message = f"{linkedin_text}: {linkedin_link}\n\n{github_text}: {github_link}"
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, disable_web_page_preview=True)

def unknown_text(update: Update, context):
    message = "'{}' is not even a command, you dumb cunt!".format(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def unknown(update: Update, context):
    message = "WTF man? Are you a fuckin dumb?\nI told you what commands I understand.\nWhat the fuck is '{}' ?".format(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', info_url))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_polling()

if __name__ == "__main__":
    main()
