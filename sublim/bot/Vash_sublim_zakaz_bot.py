# You can use this token to access HTTP API:
# 6550478011:AAFGz9ia_XCTcIiW_xpDgMRl7mZXfRIEqDk

# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

from secret import token
import telebot
from telebot import types

# для кнопки


bot = telebot.TeleBot(token)
# декорированные ожидания сообщений появятся тут

# "работа" его - ничего не делать, только ожидать сообщения


@bot.message_handler(commands=['start'])
def start(message):
    print("У меня начался рабочий день!")  # в консоль
    bot.send_message(  # Вам в Телеграм(м)
        message.chat.id,
        f'Здравствуйте, {message.from_user.first_name}!  Ваш заказ успешно сформирован!  Мы осуществляем доставку' + u'\U0001F69B' 'по всей России' + u'\U0001F1F7\U0001F1FA' 'Введите, пожалуйста адрес доставки.')


@bot.message_handler(content_types=['text'])
def reply_button(message):
    print("Новый заказ!")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        'Перейти на сайт', url='http://127.0.0.1:8000', reply_markup=markup))
    bot.reply_to(
        message, 'Благодарим. Наш менеджер свяжется с Вами, чтобы уточнить сроки доставки и способ оплаты товара.', reply_markup=markup)


bot.polling(none_stop=True)
