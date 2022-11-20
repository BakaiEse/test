import telebot

bot = telebot.TeleBot('5775923216:AAEenXtAFGIyQVAnxVpwRqP3BliOq3qmXfU')
global language

@bot.message_handler(commands=['start'])
def start_animals(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ru", callback_data="RU"),
        telebot.types.InlineKeyboardButton("En", callback_data="EN")
    )
    question = "Choose your language.\n Выберите свой язык."
    bot.send_message(message.chat.id,text=question,reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_animals(message):
    if language == "EN":
        bot.send_message(message.chat.id,''
                                     '______________________________*INDEX*____________________________\n'
                         '"/start" Is the command to start the program.\n'
                         '"/help" Is the command to find the index.\n'
                         '"/all" Is the command for me to show you all the animals that I have in my catalog.\n'
                         '"or" You can write a animal down below and I will show you a picture and a breif explanation about your animal.')
    elif language == "RU":
        bot.send_message(message.chat.id, ''
                                     '____________________________***ИНДЕКС*____________________________\n'
                         '"/start" — это команда для запуска программы.\n'
                         '"/help" Команда для поиска индекса.\n'
                         '"/all" Команда показать вам всех животных, которые есть в моем каталоге.\n'
                         '"или" Вы можете написать животное ниже, и я покажу вам изображение и краткое объяснение вашего животного.')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global language
    if call.data == "EN":
        language = "EN"
        bot.send_message(call.message.chat.id, 'Hello my name is animal_bot\n'
                              'I am here to help you learn about animals.\n'
                              'To get start please write the name of your animal.\n'
                              'If you want to learn all of the commands that I provide please write\n'
                              '"/help". ')
    elif call.data == "RU:":
        language = "Ru"
        bot.send_message(call.message.chat.id, 'Привет, меня зовут animal_bot\n'
                              'Я здесь, чтобы помочь вам узнать о животных.\n'
                              'Для начала напишите имя вашего животного.\n'
                              'Если вы хотите изучить все команды, которые я предоставляю, пожалуйста, напишите\n'
                              '"/help". ')

@bot.message_handler(func=lambda message:True)
def animal_search(message):
    photo = open(f"{language}/{message.text}.jpg","rb")
    bot.send_photo(message.chat.id,photo)
    with open(f"{language}/{message.text}.txt","r")as f:
        a = f.read()
        bot.send_message(message.chat.id,a)

bot.infinity_polling()