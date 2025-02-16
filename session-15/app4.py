import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )


async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def translate(update: Update, context):
    word= ' '.join(context.args)
    await update.message.reply_text((word))
    
if __name__ == '__main__':
    proxy_url = "socks5://127.0.0.1:1080"
    application = ApplicationBuilder().token("7389068787:AAFq-t06qBROyKWnfhZpITzRqfflAFRkbQM").proxy(
    proxy_url).get_updates_proxy(proxy_url).build()

    start_handler = CommandHandler('start', start)
    translate_handler = CommandHandler('translate', translate)
    application.add_handler(start_handler)
    application.add_handler(translate_handler)
    application.run_polling()
    
