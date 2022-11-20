import telebot

bot = telebot.TeleBot("5775923216:AAEenXtAFGIyQVAnxVpwRqP3BliOq3qmXfU")

@bot.message_handler(commands=["start"])