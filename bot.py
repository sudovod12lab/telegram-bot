import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# =======================
# Получаем токен и прокси из Railway Secrets
# =======================
import os
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
PROXY = os.environ.get("PROXY")  # например: "socks5://IP:PORT", оставь пустым если не нужен

# =======================
# Команда /start
# =======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 🤖\nЯ твой бот. Напиши задание, и я помогу его решить!"
    )

# =======================
# Создание приложения бота
# =======================
builder = ApplicationBuilder().token(TELEGRAM_TOKEN)

if PROXY:
    builder = builder.proxy_url(PROXY)

app = builder.build()

# Добавляем обработчик команды /start
app.add_handler(CommandHandler("start", start))

# =======================
# Запуск бота
# =======================
print("Бот запущен...")
try:
    app.run_polling()
except Exception as e:
    print("Ошибка при запуске бота:", e)
