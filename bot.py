import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# ✅ Рабочий SOCKS5
PROXY = "socks5://103.149.162.195:80"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Получен /start")
    await update.message.reply_text("Привет! 🤖 Я жив!")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).proxy_url(PROXY).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущен...")
app.run_polling()
