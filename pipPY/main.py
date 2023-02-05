from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc


app = ApplicationBuilder().token('token').build()

app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("sum", bc.sum_command))
app.add_handler(CommandHandler("time2ny", bc.time2ny_command))
app.add_handler(CommandHandler("xo", bc.xo_command))

app.run_polling()