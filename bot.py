import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8847798692:AAH8FDIxWjzjgc_gec49JwRzP47LrmfXm40"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [
        ['📋 ዕቃዎች ዋጋ ዝርዝር', '🧮 የBoQ ስሌት'],
        ['👷 የባለሙያ መዝገብ', '🚚 የትራንስፖርት አገልግሎት']
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    update.message.reply_text('እንኳን ወደ ጀሚኒ እንዝርት አጠቃላይ የፊኒሽንግ ስራ ቦት በደህና መጡ!', reply_markup=markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

