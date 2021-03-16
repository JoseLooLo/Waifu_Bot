
from .waifu import Waifu
from servicos.db import DB

class Group:
    def __init__(self):
        self.database = DB()

    def insertGroup(self, group_id, group_name):
        self.database.newGroup(group_id, group_name)

    def getRandomAnimeWaifu(self, group_id):
        waifu = self.database.getRandomAnimeWaifu(group_id)
        waifu_r = Waifu()
        if waifu is not None:
            waifu_r.setGender(str(waifu[3]))
            waifu_r.setImg(str(waifu[4]))
            return waifu_r
        else:
            return None

    def getAnimeWaifusByName(self, name):
        waifus = self.database.getAnimeWaifusByName(name)
        waifus_r = []
        for waifu in waifus:
            w = Waifu()
            w.setID(int(waifu[0]))
            w.setName(str(waifu[1]))
            w.setAnime(str(waifu[5]))
            w.setGender(str(waifu[3]))
            w.setImg(str(waifu[4]))
            waifus_r.append(w)

        return waifus_r

    def haveAnimeWaifuMarried(self, group_id, waifu_id):
        return self.database.haveAnimeWaifuMarried(group_id, waifu_id)

    def getCurrentWaifu(self, group_id):
        waifu = self.database.getCurrentWaifu(group_id)
        if len(waifu) == 0:
            return None
        else:
            w = Waifu()
            w.setID(int(waifu[0]))
            w.setName(str(waifu[1]))
            w.setNickname(str(waifu[2]))
            w.setAnime(str(waifu[5]))
            return w


    def getMarried(self, group_id, user_id, waifu_id, waifu_name):
        return self.database.getMarried(group_id, user_id, waifu_id, waifu_name)

    def getCurrentHarem(self, group_id, user_id):
        waifus = self.database.getCurrentHarem(group_id, user_id, 0, 0)
        waifu_r = []
        for waifu in waifus:
            w = Waifu()
            w.setName(str(waifu[1]))
            w.setAnime(str(waifu[5]))
            waifu_r.append(w)

        return waifu_r

    def removeGroupWaifus(self, number):
        return self.database.removeGroupWaifus(number)

    def getReadyGroups(self, number):
        return self.database.getReadyGroups(number)

    def getNewInterval(self):
        return self.database.newInterval()