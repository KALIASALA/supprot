import telebot
from telebot import types  # Импортируем типы для клавиатуры

bot = telebot.TeleBot('7491384700:AAEeRyGvZIh7WYxLCntHAgVDt8lcHzNE01w')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Убираем клавиатуру с кнопками
    markup = types.ReplyKeyboardRemove()

    # Создаем инлайн-клавиатуру с одной кнопкой
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="ASSIST", url="https://t.me/BizSupportMe_bot/BizSupportMe")
    keyboard.add(url_button)

    # Отправляем фото
    photo_file = open('img/Designertg.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo_file)

    # Отправляем приветственное сообщение с инлайн-клавиатурой
    bot.send_message(message.chat.id, 
        'I am incredibly passionate about transforming my dream into a thriving business venture, and I am at a crucial juncture where securing financial support is pivotal. 💼 Every ounce of assistance, no matter how small, holds immense value to me. 🌟 I am deeply grateful for the generosity and support of every kind soul willing to contribute to my journey. 🙏 Your belief in my vision means the world to me and fuels my determination to turn this dream into reality. 💪 Together, we can create something truly special and impactful. 🌍 Thank you from the bottom of my heart for considering and supporting my entrepreneurial journey. ❤️',
        reply_markup=keyboard)

bot.polling(none_stop=True)
# 7491384700:AAEeRyGvZIh7WYxLCntHAgVDt8lcHzNE01w