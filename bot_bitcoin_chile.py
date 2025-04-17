import telebot
import threading

from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
print(f"TELEGRAM_TOKEN: '{TELEGRAM_TOKEN}'")  # Depuración

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    """welcome to user"""
    bot.reply_to(message, "Bienvenido al bot Bitcoin-Precio al instante " + "\n"
                          "✰ ℒiℯხřℯ_ďℯ_₿ọt 🄰🄻🄴🅁🅃 ✰" + "\n"
                          "El bot esta en reparacion y en proceso de busqueda de servidor" + "\n")            

# comandos del bot

@bot.message_handler(commands=["btc", "eth", "dominance", "last ATH"])
def price_command(message):
    mensaje_text = message.text
    if '/btc' in mensaje_text.lower(): #  in ['/btc', '/BTC', '/bitcoin']:
        # url = "https://www.tradingview.com/symbols/BTCUSD/?exchange=BITSTAMP"
        print("precio de bitcoin")
        bot.send_message(message.chat.id, "Numbers goes up!" )
    if '/dominance' in mensaje_text.lower(): #  in ['/btc', '/BTC', '/bitcoin']:
        # url = "https://www.tradingview.com/symbols/BTCUSD/?exchange=BITSTAMP"
        print("Dominancia de bitcoin")
        bot.send_message(message.chat.id, "Muy alta, tristemente para los shitcoinlovers" )
    if '/eth' in mensaje_text.lower(): #  in ['/btc', '/BTC', '/bitcoin']:
        # url = "https://www.tradingview.com/symbols/BTCUSD/?exchange=BITSTAMP"
        print("precio de ethereum")
        bot.send_message(message.chat.id, "Numbers goes down!" )
    if '/last ATH' in mensaje_text.lower(): #  in ['/btc', '/BTC', '/bitcoin']:
        # url = "https://www.tradingview.com/symbols/BTCUSD/?exchange=BITSTAMP"
        print("Ultimo ATH de bitcoin")
        bot.send_message(message.chat.id, " $109.000 USD " )


#*************MAIN
if __name__ == "__main__":
    print("Start the bot")
    bot.infinity_polling()
    print("end")
#*************END
    