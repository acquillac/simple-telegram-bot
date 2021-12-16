import Constants as keys
# setting api keys in Constants.py example API_KEY = 'your key'
from telegram.ext import *
import responses as R 

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started')

def help_command(update, context):
    update.message.reply_text('I you need help you should ask on google')

def handle_message(update, context):
    # Recives message
    text = str(update.message.text).lower()
    response = R.sample_res(text)

    # Response
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()