import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токен бота (получи у @BotFather)
TOKEN = "8860317333:AAESFREbd0yhvyGg-UrZLb9At7VO718ZccM"

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Список аниме-животных (названия и ссылки на картинки)
anime_animals = [
    {
        "name": "Пикачу",
        "image": "https://i.pinimg.com/originals/3a/3f/6e/3a3f6e3b8f7e8b9c8d9f8e7b6c5d4e3f.jpg",
        "description": "Электрический покемон, любит кетчуп"
    },
    {
        "name": "Тоторо",
        "image": "https://i.pinimg.com/originals/4b/4c/4d/4b4c4d4e4f4g4h4i4j4k4l4m4n4o4p.jpg",
        "description": "Лесной дух из фильма 'Мой сосед Тоторо'"
    },
    {
        "name": "Джоджо-кот",
        "image": "https://i.pinimg.com/originals/5c/5d/5e/5c5d5e5f5g5h5i5j5k5l5m5n5o5p5q.jpg",
        "description": "Кот в стиле Джоджо, очень мемный"
    },
    {
        "name": "Панда-самурай",
        "image": "https://i.pinimg.com/originals/6d/6e/6f/6d6e6f6g6h6i6j6k6l6m6n6o6p6q6r.jpg",
        "description": "Панда с катаной, защитник слабых"
    },
    {
        "name": "Лис-оборотень",
        "image": "https://i.pinimg.com/originals/7e/7f/7g/7e7f7g7h7i7j7k7l7m7n7o7p7q7r7s.jpg",
        "description": "Девятихвостый лис из японских легенд"
    },
    {
        "name": "Кролик-ниндзя",
        "image": "https://i.pinimg.com/originals/8f/8g/8h/8f8g8h8i8j8k8l8m8n8o8p8q8r8s8t.jpg",
        "description": "Скрытный кролик в стиле аниме"
    },
    {
        "name": "Дракон-чиби",
        "image": "https://i.pinimg.com/originals/9g/9h/9i/9g9h9i9j9k9l9m9n9o9p9q9r9s9t9u.jpg",
        "description": "Маленький дракончик с большими глазами"
    }
]


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с кнопкой
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("🎌 Случайное аниме-животное", callback_data="random_animal")
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "Привет! Я бот, который показывает случайных животных в стиле аниме! 🐱🎌\n\nНажми на кнопку ниже, чтобы получить случайное животное:",
        reply_markup=markup
    )


# Обработчик нажатия на кнопку
@bot.callback_query_handler(func=lambda call: call.data == "random_animal")
def send_random_animal(call):
    # Выбираем случайное животное
    animal = random.choice(anime_animals)

    # Отправляем картинку с подписью
    caption = f"✨ {animal['name']}\n📝 {animal['description']}"

    try:
        # Отправляем фото
        bot.send_photo(
            call.message.chat.id,
            animal['image'],
            caption=caption
        )
    except Exception as e:
        # Если картинка не загружается, отправляем текстовое сообщение
        bot.send_message(
            call.message.chat.id,
            f"✨ {animal['name']}\n📝 {animal['description']}\n\n🖼 К сожалению, картинка не загрузилась :("
        )

    # Показываем кнопку снова, чтобы можно было получить ещё одно животное
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("🎌 Ещё одно животное", callback_data="random_animal")
    markup.add(button)

    bot.send_message(
        call.message.chat.id,
        "Хочешь увидеть ещё одно животное? Нажми на кнопку!",
        reply_markup=markup
    )


# Обработчик для обычных сообщений (если пользователь что-то пишет)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(
        message,
        "Используй кнопку 'Случайное аниме-животное' чтобы получить животное! 🎌"
    )


# Запуск бота
if __name__ == "__main__":
    print("Бот запущен и готов к работе!")
    bot.infinity_polling()