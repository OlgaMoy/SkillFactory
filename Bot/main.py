import telebot
from config import keys, TOKEN
from exception import APIException, ValueConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help']) #создаем описание для команд старт и помощь
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n<Имя валюты, цену которой вы хотите узнать> \
<Имя валюты, в которой хотите узнать цену> \
<количество переводимой валюты>\nПосмотреть спискок всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values']) #создаем описание для команды валюты
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ]) #выводим сообщение о результатах конвертации
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Указано неверное количество параметров. Проверьте правильность ввода с помощью команды /help.')

        quote, base, amount = values
        total_base = ValueConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()