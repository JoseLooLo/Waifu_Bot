from domain.bot import Bot
import telegram
from telegram import Message
from domain.group import Group
from domain.waifu import Waifu
from domain.responses import Responses
import util
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, RegexHandler, Filters, CallbackContext


def main():
    bot = Bot()
    updater = Updater('1134043476:AAFRo6bqfeeiNljslBvLKQEtNuD_jppRHjc', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',bot.start))          #Initial msg
    dp.add_handler(CommandHandler('help',bot.help))            #Help
    dp.add_handler(CommandHandler('waifu',bot.waifu))          #New waifus
    dp.add_handler(CommandHandler('marry',bot.marry))          #Marry with current waifu
    dp.add_handler(CommandHandler('harem',bot.harem))          #List the current harem
    dp.add_handler(CommandHandler('awaifu',bot.awaifu))          #Show Anime Waifu
    dp.add_handler(CommandHandler('mwaifu',bot.mwaifu))          #Show Manga Waifu
    j = updater.job_queue
    j.run_repeating(bot.remove_waifus, interval=10, first=0)    #Remove waifus
    j.run_repeating(bot.waifus, 1)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()