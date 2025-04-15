from config import *
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)
@bot.message_handler(commands=['start'])
def cmd_start(message):
    """welcome to user"""
    bot.reply_to(message, "Hola, como andamios!")
    #bot.send_message(message.chat.id, "Hola, soy un bot de prueba. ¿Cómo puedo ayudarte?")

#*************MAIN
if __name__ == "__main__":
    print("Start the bot")
    bot.infinity_polling()
    print("end")
    