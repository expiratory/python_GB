from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc


app = ApplicationBuilder().token('token').build()

app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("sum", bc.sum_command))

app.run_polling()

# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()


# from isOdd import isOdd

# print(isOdd(4))
# print(isOdd(1))