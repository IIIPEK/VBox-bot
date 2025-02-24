import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Функция для обработки всех текстовых сообщений
async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Этот бот лежит на локальном сервере")

# Основная функция для запуска бота
def main():
    # Вставьте сюда токен вашего бота
    TOKEN = '7382775995:AAEutjm3OtH0B7CSUJ8OfYdhq-KsdLhpBVo'

    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчик для всех текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))

    # Запускаем бота
    print("Бот запущен...")
    try:
        application.run_polling()
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")

    print("Бот остановлен.")

if __name__ == '__main__':
    main()