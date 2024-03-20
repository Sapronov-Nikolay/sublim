from secret import token
import telebot
from telebot import types

# для кнопки


bot = telebot.TeleBot(token)
# декорированные ожидания сообщений появятся тут

# "работа" его - ничего не делать, только ожидать сообщения


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id,
                     "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        'Перейти на сайт', url='http://127.0.0.1:8000', reply_markup=markup))

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Мой регион Москва')
        btn2 = types.KeyboardButton('Другой регион')

        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         f'Здравствуйте, {message.from_user.first_name}!  Ваш заказ успешно сформирован!  Мы осуществляем доставку' + u'\U0001F69B' 'по всей России' + u'\U0001F1F7\U0001F1FA', reply_markup=markup)

    elif message.text == 'Мой регион Москва':
        bot.send_message(
            message.from_user.id, 'Благодарим. Наш менеджер свяжется с Вами, чтобы уточнить сроки доставки и способ оплаты товара.', reply_markup=markup)

    elif message.text == 'Другой регион':
        bot.send_message(
            message.from_user.id, 'Благодарим. Наш менеджер свяжется с Вами, чтобы уточнить сроки доставки и способ оплаты товара.', reply_markup=markup)


bot.polling(none_stop=True)
