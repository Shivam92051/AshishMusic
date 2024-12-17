from AshishX.core.bot import ASHISH
from AshishX.core.dir import dirr
from AshishX.core.git import git
from AshishX.core.userbot import Userbot
from AshishX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ASHISH()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
