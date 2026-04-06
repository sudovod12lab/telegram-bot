import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# ✅ MTProto прокси (HTTP)
request = HTTPXRequest(
    proxy_url="http://proxy.mtproto.me:443"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Получен /start")
    await update.message.reply_text("Привет! 🤖 Я жив!")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(request).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущен...")
app.run_polling()
