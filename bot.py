import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# የሎግ ማስተካከያ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """የ /start ትዕዛዝ ሲጻፍ የሚሰጥ ምላሽ"""
    await update.message.reply_text('ሰላም! የቴሌግራም ቦትዎ በትክክል እየሰራ ነው።')

def main():
    # ከሬንደር Environment Variables ላይ ቶከኑን መቀበል
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("ስህተት: BOT_TOKEN አልተገኘም!")

    # ቦቱን መገንባት
    application = ApplicationBuilder().token(token).build()
    
    # ትዕዛዞችን ማገናኘት
    application.add_handler(CommandHandler("start", start))
    
    # ቦቱን ማስጀመር
    print("ቦቱ በመጀመር ላይ ነው...")
    application.run_polling()

if __name__ == '__main__':
    main()
