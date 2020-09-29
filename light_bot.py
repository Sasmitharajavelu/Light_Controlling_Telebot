
from Adafruit_IO import Client, Feed, Data #import libraries
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import os

ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME') #Get keys,username,token
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY')
token_telegram = os.getenv('token_telegram')

newfeed = Feed(name = 'hellolightbot') #create feed
result = aio.create_feed(newfeed)

def start(bot, update): #func for start command
    bot.send_message(chat_id = update.effective_chat.id, text="__hello telegrammer__")
    bot.send_message(chat_id = update.effective_chat.id, text="Do you want to turn on the light YES? type 'Turn on the light' NO then type 'Turn off the light'")

def invalid(bot, update): #func for improper commands
    bot.send_message(chat_id=update.effective_chat.id, text="Very sorry,that is invalid.Try again!")

def send_data_adafruit(value1): #func to send data
  value = Data(value=value1)
  value_send = aio.create_data('hellolightbot',value)  

def light_off(bot, update): #func for turning on light
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Here we go turning off")
  bot.send_photo(chat_id, photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  bot.send_message(chat_id, text="Do you like to turn on?")
  bot.send_message(chat_id, text="If yes,type'Turn on the light',else type'No'")
  send_data_adafruit(0)

def light_on(bot, update): #func for turning off light
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Here we go turning on")
  bot.send_photo(chat_id=update.effective_chat.id,photo='http://scienceblog.cancerresearchuk.org/wp-content/uploads/2015/08/Lightbulb_hero2.jpg')
  bot.send_message(chat_id, text="Do you like to turn off?")
  bot.send_message(chat_id, text="If yes,type'Turn off the light',else type'No'")
  send_data_adafruit(1)

def the_end(bot, update): #func for ending bot
    bot.send_message(chat_id=update.effective_chat.id, text="Waiting for the command")  

def commands(bot, update): #calling func with respect to commands
  text = update.message.text
  if text == 'Start':
    start(bot,update)
  elif text == 'Turn off the light':
     light_off(bot, update)
  elif text == 'Turn on the light':
     light_on(bot,update)
  elif text == 'No':
     the_end(bot,update)
  else:
     invalid(bot,update)
    
ur = Updater('token_telegram')
dp = ur.dispatcher
dp.add_handler(MessageHandler(Filters.text, commands))
ur.start_polling()
ur.idle()
