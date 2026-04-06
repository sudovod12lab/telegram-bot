from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError("❌ Токен НЕ найден!")

print("✅ Токен есть")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Получен /start")
    await update.message.reply_text("Привет! 🤖 Я жив!")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🚀 Бот запускается...")
app.run_polling()
