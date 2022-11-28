from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def start(bot, update):
    update.message.reply_text('Привет! Я бот для заказов от Мудреца Липси! .\n'
                              'Для получения информации можете воспользоваться подсказками ниже!',
                              reply_markup=markup)
    
def close_keyboard(bot, update):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())    

def echo(bot, update):
    if update.message.text[-1] == '?':
        update.message.reply_text('Конечно можно спросить! Только я культурно промолчу...')
    else:
        update.message.reply_text('Вполне возможно, кто ж знает?')
    
def deanonprice(bot, update):
    update.message.reply_text("""
Прайс-Лист на услуги деанона:

Пробив по ФИО(Любое ГЕО) - 150₽
Пробив по номеру телефона(РФ) - 100₽
Пробив по номеру телефона(УКР) - 150₽
Пробив по ВКонтакте(Любое ГЕО) - 200₽
Пробив по Telegram(Любое ГЕО) - 200₽
Пробив по гос. номеру а/м (РФ) - 350₽
Пробив ООО/ИП/ИНН (РФ) - 50₽
Заказ еды на дом (РФ) - 10₽/Доставка 
Заказ сексшопа на дом (РФ) - 25₽/Доставка

@lipsiprice_bot - Лучший пробив в Telegram
"""



def contact(bot, update):
    update.message.reply_text("Официальный контакт: @lipsi_mudrec")

def work_time(bot, update):
    update.message.reply_text('Время работы: пн-вс, 9:00 - 23:00')


updater = Updater('5811231521:AAGiEnXmK2grpp-ERqB2n4Y1Qfkgn08DMWE')

dp = updater.dispatcher

reply_keyboard = [['/close', '/deanonprice'],
                  ['/contact', '/work_time']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('close', close_keyboard))
dp.add_handler(CommandHandler('contact', contact))
dp.add_handler(CommandHandler('work_time', work_time))
dp.add_handler(CommandHandler('deanonprice', deanonprice))

text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)

updater.start_polling()

updater.idle()