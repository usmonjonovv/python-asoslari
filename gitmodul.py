import telebot
TOKEN = '7191164391:AAGf3NIludQER9v_M1dUeM6hvIqTZZX10PY'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalamu Alaykum! Xush kelibsiz.")
	