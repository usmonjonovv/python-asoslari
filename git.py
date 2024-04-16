from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '7191164391:AAGf3NIludQER9v_M1dUeM6hvIqTZZX10PY'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['start'])

def send_welcome(message):
	javob = "Assalamu Alaykum! Xush kelibsiz."
	javob+= "\nMatn kiriting: "
	bot.reply_to(message,javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

bot.infinity_polling()