
class Responses:
    def __init__(self):
        self.create_emojis()
        self.create_msgs()

    def create_emojis(self):
        self.EMOJI_F = u'\U0001F6BA' #Girl Emoji
        self.EMOJI_M = u'\U0001F6B9' #Male Emoji
        self.EMOJI_N = u'\U00002753' #Neutral Emoji ??
        self.EMOJI_RING = u'\U0001F48D' #Anel

    def create_msgs(self):
        self.RUN_MSG = "Waifu has run away..."

        self.WILD_WAIFU = "A wild waifu has appeared!\n\
        Use /marry <name/nickname of the character> to capture it."

        self.NENHUMA_WAIFU = "No waifu was seen in the surroundings."

        self.WILD_F_WAIFU = self.EMOJI_F + " " + self.WILD_WAIFU

        self.WILD_M_WAIFU = self.EMOJI_M + " " + self.WILD_WAIFU

        self.WILD_N_WAIFU = self.EMOJI_N + " " + self.WILD_WAIFU

        self.CASAMENTO = "You married " + self.EMOJI_RING + " !!"

        self.START = "Welcom to waifu teste bot!\n\
        Randomly a  waifu will appear in here, \
        just typing /marry <nome> to marry.\n\
        Use /help to find other commands."

        self.HELP = "Commands:\n\
        /marry <name>\n\
        -To marry\n\
        /waifu\n\
        -A new waifu will appear\n\
        /harem\n\
        -View your waifus\n"

        self.RUN_MSG_2 = "Sadly the waifu is running away right now."

        self.CASAMENTO_2 = "Sadly this waifu has an owner already.\n\
        The time for a new waifu will be reduced."

        self.MARRY_WITHOUT_MSG = "You need to type the name of the waifu right \
        after the command /marry <name>.\n"

        self.MARRY_INCORRECT_MSG = "Hmm.. Sadly this is not the name of this little pretty one.\n"

        self.NO_ARGS = "Need to type the name of a waifu..."

        self.MUITAS_WAIFUS = "There's too many waifus with this name. Be more specific."

        self.LIST_WAIFUS_AWAIFU = "Found some waifus.\n\
        Type the command again with the waifu's full name.\n"

        self.NO_WAIFU = "Nenhuma waifu encontrada.."
