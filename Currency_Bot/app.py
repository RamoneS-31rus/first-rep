import telebot
from config import keys, TOKEN
from extensions import ConvertionException, Get_price

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Формат ввода: \n\
<конвертируемая валюта> <в какую валюту перевести> <количество конвертируемой валюты>  \n\
Пример ввода: доллар рубль 1 \n\
Список команд: \n\
/values - доступные валюты'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        values = [x.lower() for x in values]

        if len(values) != 3:
            raise ConvertionException('Некорректное количество параметров.')

        base, quote, amount = values
        total_base = Get_price.convert(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка ввода:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду: \n{e}')
    else:
        text = f'{amount} {base} = {total_base} {quote}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)