from config import *
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hola, soy un bot de prueba. ¿Cómo puedo ayudarte?")
