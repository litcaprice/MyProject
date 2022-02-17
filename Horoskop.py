import telebot

bot = telebot.TeleBot("5225587018:AAHMQjOEwuvCgnfcuzFvaHNdh3sFnHCpNrU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Пока")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
