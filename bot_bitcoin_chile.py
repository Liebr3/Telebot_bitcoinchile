import telebot
import threading
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
print(f"TELEGRAM_TOKEN: '{TELEGRAM_TOKEN}'")  # Depuración
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# bienvenida al usuario

@bot.message_handler(commands=['start'])
def cmd_start(message):
    """welcome to user"""
    bot.reply_to(message, "Bienvenido al bot Bitcoin-Precio al instante " + "\n"
                          "✰ ℒiℯხřℯ_ďℯ_₿ọt 🄰🄻🄴🅁🅃 ✰" + "\n"
                          "El bot esta en reparacion y en proceso de busqueda de servidor" + "\n")            

# comandos del bot

@bot.message_handler(commands=["btc", "eth", "dominance", "ath"])
def price_command(message):
    mensaje_text = message.text
    if '/btc' in mensaje_text.lower(): 
        print("precio de bitcoin")
        bot.send_message(message.chat.id, "Numbers goes up!" )
    if '/dominance' in mensaje_text.lower(): 
        print("Dominancia de bitcoin")
        bot.send_message(message.chat.id, "Muy alta, tristemente para los shitcoinlovers" )
    if '/eth' in mensaje_text.lower(): 
        print("precio de ethereum")
        bot.send_message(message.chat.id, "Numbers goes down!" )
    if '/ath' in mensaje_text.lower(): 
        print("Ultimo ATH de bitcoin")
        bot.send_message(message.chat.id, " $109.000 USD " )



def recibir_mensajes():
    bot.infinity_polling()


bot.set_my_commands([
    telebot.types.BotCommand("/start", "Descripción del bot"),
    telebot.types.BotCommand("/btc", "BTC/USD"),
    telebot.types.BotCommand("/eth", "ETH/USD"),
    telebot.types.BotCommand("/dominance", "Dominancia de BTC"),
    telebot.types.BotCommand("/ath", "Ultimo ATH de BTC")])


#*************MAIN
if __name__ == "__main__":

    
    print("Start the bot")
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    
    print("end")
#*************END
    