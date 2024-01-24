from secret import token
import telebot

bot = telebot.TeleBot(token)
# декорированные ожидания сообщений появятся тут

#"работа" его - ничего не делать, только ожидать сообщения


@bot.message_handler()
def start(message):
    print ("У меня начался рабочий день!")  # в консоль
    bot.send_message(  # Вам в Телеграм(м)
        message.chat.id,
        '<b>С наступающим Новым Годом!!! ХО-ХО-ХО!!!)</b>',
        parse_mode='html')
    

bot.polling(none_stop=True)