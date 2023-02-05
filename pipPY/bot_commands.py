from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime as dt
import spy

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await spy.log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await spy.log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/time2ny')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await spy.log(update, context)
    await update.message.reply_text(f'{dt.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await spy.log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def time2ny_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await spy.log(update, context)
    now = dt.datetime.today()
    NY = dt.datetime(2024,1,1)
    d = NY - now
    await update.message.reply_text(f'Дл НГ осталось {d}')

async def xo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await spy.log(update, context)
    playground = ('7 8 9\n'
                 +'4 5 6\n'
                 +'1 2 3\n')
    p_choise = int(input('Выберите клетку: '))
    
    await update.message.reply_text(f'')