import random
import telebot


TOKEN = "9121440085:AAH1vqlom7Vyjh-ikCDwc5uRX4GYXfAAMKc"
bot = telebot.TeleBot(TOKEN)

# Список шуточных ответов
ANSWERS = [
    "Даже не думай этого делать",
    "Посоветуйся с подружкой",
    "Звезды говорят: давно пора",
    "Звезды говорят: Туз Червей у тебя"
    "подпишись на инсту @lt8nnn и @diswexq, спасибо",
    "100% да, но только если ты съешь банан)",
    "Звезды говорят: лучше поспи 😴",
    "Ответ скрыт в треке Честный - Майами! 🎧",
    "Нет, но если включить басы погромче — возможно тебе повезёт🔊",
    "Даже искусственный интеллект в шоке от этого вопроса, лучше спроси у Вани 🤯",
    "Спроси после того, как послушаешь Сектор Газа 🎸"
    "Ты выглядишь прекрасно!" ,
]

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Привет! Я Бот-Ыван и будущий Музыкальный Плеер 🎵\n"
        "Задай мне любой вопрос, и я предскажу твоё будущее!"
    )

# Обработка любых текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = random.choice(ANSWERS)
    bot.reply_to(message, answer)

# Запуск постоянного опроса серверов Telegram
print("Бот запущен и ждет сообщения...")
bot.polling(none_stop=True)
