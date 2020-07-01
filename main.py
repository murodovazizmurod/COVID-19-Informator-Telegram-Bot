import telebot
from telebot import types
import config
import covid19cases as covid

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    sticker = open('sticker_three.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    hello_text = "So'ngi ma'lumotlarni olish uchun davlatni tanlang"

    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Aqsh')
    itembtnr = types.KeyboardButton('Rossiya')
    itembtnx = types.KeyboardButton('Xitoy')
    itembtni = types.KeyboardButton('Ispaniya')
    itembtnit = types.KeyboardButton('Italiya')
    itembtnu = types.KeyboardButton('O\'zbekiston')
    markup.add(itembtna, itembtnx, itembtnr,itembtni, itembtnit, itembtnu)
    bot.send_message(message.chat.id, hello_text, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def corona(message):
    if message.text == 'Aqsh':
        res = covid.get_country_cases("USA")
    elif message.text == 'Ispaniya':
        res = covid.get_country_cases("Spain")
    elif message.text == 'Rossiya':
        res = covid.get_country_cases("Russia")
    elif message.text == 'O\'zbekiston':
        res = covid.get_country_cases("Uzbekistan")
    elif message.text == 'Buyuk Britaniya':
        res = covid.get_country_cases("UK")
    elif message.text == 'Italiya':
        res = covid.get_country_cases("Italy")
    elif message.text == 'Fransiya':
        res = covid.get_country_cases("France")
    elif message.text == 'Germaniya':
        res = covid.get_country_cases("Germany")
    elif message.text == 'Turkiya':
        res = covid.get_country_cases("Turkey")
    elif message.text == 'Xitoy':
        res = covid.get_country_cases("China")
    else:
        res = covid.get_global_cases()


    lat = res['TotalCases']
    new = res['NewCases']
    deth = res['TotalDeaths']
    rec = res['TotalRecovered']
    text = "Jami kasallanganlar soni: {0}\nBugun aniqlangan bemorlar soni: {1}\nJami o'limlar soni: {2}\nJami tuzalganlar soni: {3}\nAgarda bu sonlar ortishini istamasangiz <b>Uyda qoling</b>".format(lat, new.replace("+", ""), deth, rec)
    bot.send_message(message.chat.id, text, parse_mode='html')

if __name__ == '__main__':
    bot.polling(none_stop=True)
