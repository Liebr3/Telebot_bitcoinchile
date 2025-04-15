import telebot

from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    """welcome to user"""
    bot.reply_to(message, "Bienvenido al bot Bitcoin-Precio al instante " + "\n"
                          "Cuando liebr3 y Copilot terminen les daré el precio "
                          "de Bitcoin y otros valores en tiempo real" + "\n")            

#*************MAIN
if __name__ == "__main__":
    print("Start the bot")
    bot.infinity_polling()
    print("end")
#*************END
    