import telegram
from telegram import Message
from domain.group import Group
from domain.waifu import Waifu
from domain.responses import Responses
import util
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, RegexHandler, Filters, CallbackContext

class Bot:
    def __init__(self):
        self.group = Group()
        self.response = Responses()

    def start(self, update, context):
        try:
            group_id = update.effective_chat.id
            group_name = ""
            if update.effective_chat.title:
                group_name = update.effective_chat.title
            self.group.insertGroup(group_id, group_name)
            waifu_img_ex = "https://cdn.myanimelist.net/images/characters/2/257273.jpg"
            context.bot.send_photo(chat_id=group_id, photo=waifu_img_ex, caption=self.response.START)
        except Exception as e:
            print("[ERROR] - {}".format(e))


    def help(self, update, context):
        group_id = update.effective_chat.id
        msg_to_reply = update.message.message_id
        context.bot.send_message(chat_id=group_id, text=self.response.HELP, reply_to_message_id=msg_to_reply)

    def waifu(self, update, context):
        try:
            group_id = update.effective_chat.id
            waifu = self.group.getRandomAnimeWaifu(group_id)
            if waifu is not None:
                if waifu.genderIsF():
                    context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=self.response.WILD_F_WAIFU)
                elif waifu.genderIsM():
                    context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=self.response.WILD_M_WAIFU)
                else:
                    context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=self.response.WILD_N_WAIFU)

        except Exception as e:
            print("[ERROR] - {}".format(e))

    def awaifu(self, update, context):
        try:
            group_id = update.effective_chat.id
            msg_to_reply = update.message.message_id
            number = -1
            if len(context.args) == 0:
                context.bot.send_message(chat_id=group_id, text=self.response.NO_ARGS, reply_to_message_id=msg_to_reply)
                return

            #Verificar se há busca por indice na lista
            for arg in context.args:
                if (arg[0] == '#'):
                    try:
                        number = int(arg[1:])
                        context.args.remove(arg)
                        break
                    except Exception as e:
                        number = -1
            
            waifus = self.group.getAnimeWaifusByName(" ".join(context.args))
            if len(waifus) > 5:
                context.bot.send_message(chat_id=group_id, text=self.response.MUITAS_WAIFUS, reply_to_message_id=msg_to_reply)
            elif len(waifus) == 1:
                waifu = waifus[0]
                married = self.group.haveAnimeWaifuMarried(group_id, waifu_id)

                gender_emoji = self.response.EMOJI_N
                if waifu.genderIsF():
                    gender_emoji = self.response.EMOJI_F
                elif waifu.genderIsM():
                    gender_emoji = self.response.EMOJI_M

                if married:
                    temp_msg = "{} {} {}\n({})".format(waifu.getName(), gender_emoji, self.response.EMOJI_RING, waifu.getAnime())
                else:
                    temp_msg = "{} {}\n({})".format(waifu.getName(), gender_emoji, waifu.getAnime())

                context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=temp_msg)
            elif len(waifus) == 0:
                context.bot.send_message(chat_id=group_id, text=self.response.NO_WAIFU, reply_to_message_id=msg_to_reply)
            else:
                if number != -1 and number <= len(waifus) and number > 0:
                    waifu = waifus[number-1]
                    married = self.group.haveAnimeWaifuMarried(group_id, waifu_id)

                    gender_emoji = self.response.EMOJI_N
                    if waifu.genderIsF():
                        gender_emoji = self.response.EMOJI_F
                    elif waifu.genderIsM():
                        gender_emoji = self.response.EMOJI_M

                    if married:
                        temp_msg = "{} {} {}\n({})".format(waifu.getName(), gender_emoji, self.response.EMOJI_RING, waifu.getAnime())
                    else:
                        temp_msg = "{} {}\n({})".format(waifu.getName(), gender_emoji, waifu.getAnime())

                    context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=temp_msg)
                else:
                    msg = self.response.LIST_WAIFUS_AWAIFU + "\n"
                    count = 1
                    for waifu in waifus:
                        married = self.group.haveAnimeWaifuMarried(group_id, waifu_id)
                        if married:
                            temp_msg = "{}. {} ({}) {}\n".format(str(count), waifu.getName(), waifu.getAnime(), self.response.EMOJI_RING)
                        else:
                            temp_msg = "{}. {} ({})\n".format(str(count), waifu.getName(), waifu.getAnime())
                        count+=1
                        msg += temp_msg
                    context.bot.send_message(chat_id=group_id, text=msg, reply_to_message_id=msg_to_reply)

        except Exception as e:
            print("[ERROR] - {}".format(e))

    def mwaifu(self, update, context):
        try:
            pass
            #TODO
        except Exception as e:
            print("[ERROR] - {}".format(e))

    def marry(self, update, context):
        try:
            group_id = update.effective_chat.id
            user_id = update.message.from_user.id
            msg_to_reply = update.message.message_id
            waifu = self.group.getCurrentWaifu(group_id)
            if waifu is None:
                context.bot.send_message(chat_id=group_id, text=self.response.NENHUMA_WAIFU)
            else:
                if util.compare_names(waifu.getName(), waifu.getNickname(), context.args):
                    response = self.group.getMarried(group_id, user_id, waifu.getID(), waifu.getName())
                    if response == 0:
                        msg = self.response.CASAMENTO + "\nSua nova esposa é "+waifu.getName()+" ("+waifu.getAnime()+")\nFelicidades ao casal."
                        context.bot.send_message(chat_id=group_id, text=msg, reply_to_message_id=msg_to_reply)
                    elif response == 1:
                        context.bot.send_message(chat_id=group_id, text=self.response.RUN_MSG_2)
                    elif response == 2:
                        context.bot.send_message(chat_id=group_id, text=self.response.CASAMENTO_2)
                else:
                    if len(context.args) == 0:
                        context.bot.send_message(chat_id=group_id, text=self.response.MARRY_WITHOUT_MSG)
                    else:
                        context.bot.send_message(chat_id=group_id, text=self.response.MARRY_INCORRECT_MSG)

        except Exception as e:
            print("[ERROR] - {}".format(e))

    def harem(self, update, context):
        try:
            usr_name = update.message.from_user.first_name
            if update.message.from_user.username:
                usr_name += ' (@' + update.message.from_user.username + ')'
            
            msg_to_reply = update.message.message_id
            group_name = ""
            if update.effective_chat.title:
                group_name = update.effective_chat.title
            group_id = update.effective_chat.id
            user_id = update.message.from_user.id

            waifus = self.group.getCurrentHarem(group_id, user_id)

            msg = usr_name + " harem in " + group_name + ":\n"
            count = 1
            for waifu in waifus:
                msg_temp = str(count)+". "+waifu.getName()+" ("+waifu.getAnime()+")\n"
                msg+=msg_temp
                count += 1
            context.bot.send_message(chat_id=group_id, text=msg, reply_to_message_id=msg_to_reply)

        except Exception as e:
            print("[ERROR] - {}".format(e))

    def remove_waifus(self, context):
        try:
            job = context.job
            groups = self.group.removeGroupWaifus(job.interval)
            for group_id in groups:
                context.bot.send_message(chat_id=group_id, text=self.response.RUN_MSG)

        except Exception as e:
            print("[ERROR] - {}".format(e))

    def waifus(self, context):
        try:
            job = context.job
            groups = self.group.getReadyGroups(job.interval)

            for group_id in groups:
                waifu = self.group.getRandomAnimeWaifu(group_id)
                if waifu is not None:
                    if waifu.genderIsF():
                        context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=self.response.WILD_F_WAIFU)
                    elif waifu.genderIsM():
                        context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=self.response.WILD_M_WAIFU)
                    else:
                        context.bot.send_photo(chat_id=group_id, photo=waifu.getImg(), caption=self.response.WILD_N_WAIFU)
            
            new_interval = self.group.getNewInterval()
            if new_interval == -1:
                new_interval = 60
            job.interval = new_interval
            
        except Exception as e:
            print("[ERROR] - {}".format(e))
    
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