class Waifu:
    def __init__(self):
        self.id = -1
        self.name = ""
        self.nickname = ""
        self.anime = ""
        self.gender = ""
        self.img = ""

    def setName(self, name):
        self.name = name
    
    def setNickname(self, nick):
        self.nickname = nick

    def setGender(self, gender):
        self.gender = gender.lower()

    def setImg(self, img):
        self.img = img

    def setID(self, _id):
        self.id = _id

    def setAnime(self, anime):
        self.anime = anime

    def getName(self):
        return self.name

    def getNickname(self):
        return self.nickname

    def getGender(self):
        return self.gender

    def getImg(self):
        return self.img

    def getID(self):
        return self.id

    def getAnime(self):
        return self.anime

    def genderIsF(self):
        return self.gender == 'f'

    def genderIsM(self):
        return self.gender == 'm'