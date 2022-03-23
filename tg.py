'''
1."Back" in 'def examples' does not work 
2. It is not clear how the keyboard buttons should work at startup, 'cause state works through the menu
'''

from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Bot, keyboardbutton
from datetime import datetime
import mongodb

def _init_(TELEGRAM_TOKEN):
    global bot
    bot = Bot(TELEGRAM_TOKEN)
    Tg_cli = Updater(TELEGRAM_TOKEN)
    Tg_cli.dispatcher.add_handler(CommandHandler('start', start))
    Tg_cli.dispatcher.add_handler(MessageHandler(Filters.text, mainLogic))
    Tg_cli.start_polling()
    print("SERVER STARTED")

def start(Tg_cli: Update, context: CallbackContext) -> None:
    user = {}
    user['first_name'] = Tg_cli.effective_user.first_name
    user['id'] = Tg_cli.effective_user.id
    Tg_cli.message.reply_text(f'Hi, {Tg_cli.effective_user.first_name}!')
    mongodb.write_to_DB('UI', user)
    menu(Tg_cli, context)

def mainLogic(Tg_cli: Update, context: CallbackContext) -> None:
    text = Tg_cli.message.text
    uid = {'id': Tg_cli.effective_user.id}
    try:
        state = context.user_data['state']
    except:
        context.user_data['state'] = "menu"
        state = "menu"
        menu(Tg_cli, context)
    match state:
        case 'menu':
            if text == "Examples":
                examples(Tg_cli, context)
            elif text == "Price":
                price(Tg_cli, context)
            elif text == "Signup":
                signup(Tg_cli, context)
            else:
                Tg_cli.message.reply_text(f'{Tg_cli.effective_user.first_name}, select a button on the keyboard.')
        case 'signup':
            if text == 'Select date and time':
                Tg_cli.message.reply_text(f'Okey')
            elif text == 'Write to the master':
                Tg_cli.message.reply_text(f'@litcaprice')
            elif text == 'Back':
                menu(Tg_cli, context)
            else:
                Tg_cli.message.reply_text(f'{Tg_cli.effective_user.first_name}, select a button on the keyboard.')

def menu(Tg_cli: Update, context: CallbackContext) -> None:
    context.user_data['state'] = "menu"
    keyboard = [
        [
            KeyboardButton('Price'),
            KeyboardButton('Examples'),
            KeyboardButton('Signup')
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    Tg_cli.message.reply_text(f' You are now on the menu. Here you can find out the price, see examples from the portfolio and sign up.', reply_markup=reply_markup)

def examples(Tg_cli: Update, context: CallbackContext) -> None:
   Tg_cli.message.reply_text(f'Work examples')

def price(Tg_cli: Update, context: CallbackContext) -> None:
   Tg_cli.message.reply_text(f'Price')

def signup(Tg_cli: Update, context: CallbackContext) -> None:
    context.user_data['state'] = "signup"
    keyboard = [
        [
            KeyboardButton('Select date and time'),
            
        ],
        [
            KeyboardButton('Back'),
            KeyboardButton('Write to the master')
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    text = Tg_cli.message.text
    Tg_cli.message.reply_text(f'Select huinu', reply_markup=reply_markup)
    