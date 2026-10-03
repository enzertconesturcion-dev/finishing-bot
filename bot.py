import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8847798692:AAH8FDIxWjzjgc_gec49JwRzl3Rmon4aak8"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [
        ['📋 የእቃዎች ዋጋ ዝርዝር', '🧮 የBoQ ስሌት'],
        ['👷 የባለሙያ መዝገብ', '🚚 የትራንስፖርት አገልግሎት']
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "እንኳን ወደ የፊኒሺንግ እና ኮንስትራክሽን ገበያ ቦት በደህና መጡ!\n\nምን ማወቅ ይፈልጋሉ?",
        reply_markup=markup
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
