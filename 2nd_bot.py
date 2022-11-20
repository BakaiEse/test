import telebot

bot = telebot.TeleBot("5775923216:AAEenXtAFGIyQVAnxVpwRqP3BliOq3qmXfU")

@bot.message_handler(commands = ['start'])
def start_animals(message):
    bot.reply_to(message,'please write your animal.')

@bot.message_handler(commands=['help'])
def basket(message):
    pass

bot.infinity_polling()