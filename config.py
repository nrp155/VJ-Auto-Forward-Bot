from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "7d2ccae297d9bddc2c1a704f4db9051a")
      API_ID = int(getenv("API_ID", "4608228"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "1879736366:AAEgEsv8L90BmNn5IamLJbQFa2H4AXg-WuY")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001416144010:-1001390161207").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
