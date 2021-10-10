my_Usearname='Ayman_A_Hafez'

my_Password='Dream2412000'

#from PIL import Image

from instapy import InstaPy
session = InstaPy(username="Ayman_A_Hafez", password="Dream2412000") 
session.login()
session.like_by_tags(["football"],amount=4)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
"""
from instabot import Bot
bot = Bot()
bot.login(username="Ayman_A_Hafez", password="Aymoon2412000")
my_following=bot.following()

"""