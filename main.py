from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from weather import get_forecasts

# check for new messages --> polling
updater = Updater(token="584234825:AAG2T3KY6C2H-rNr-pswpA4r6i5mtwndQjE")

# allows to register handler -> command, text, video, audio etc
dispatcher = updater.dispatcher


# define a command callback function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, Welcome to WeatherXYZ....")


# create a command handler
start_handler = CommandHandler("start", start)

# add command handler to dispatcher
dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text.upper())


# create a text handler
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(echo_handler)


def option(bot, update):
    button = [
        [InlineKeyboardButton("Option 1", callback_data="1"),
         InlineKeyboardButton("Option 2", callback_data="2")],
        [InlineKeyboardButton("Option 3", callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Choose one option..",
                     reply_markup=reply_markup)


option_handler = CommandHandler("option", option)
dispatcher.add_handler(option_handler)


def get_location(bot, update):
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Mind sharing location?",
                     reply_markup=reply_markup)


get_location_handler = CommandHandler("location", get_location)
dispatcher.add_handler(get_location_handler)


def location(bot, update):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    forecasts = get_forecasts(lat, lon)
    bot.send_message(chat_id=update.message.chat_id,
                     text=forecasts,
                     reply_markup=ReplyKeyboardRemove())


location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)

# start polling
updater.start_polling()
