import json
import random

from cogs.cog_gamble import Gambling
from cogs.cog_math import Mathematics
from cogs.cog_admin import Administration
from cogs.cog_news import News


def printLogo():
    with open("./res/logo.txt") as f:
        for i in f:
            print(i)


def init() -> dict:
    printLogo()
    print("--- Init Phase ---")
    random.seed()
    print("  Random seed ok")
    with open("config.json") as f:
        config = json.load(f)
        print("  Config options set")
    return config


def loadCogs(bot):
    bot.add_cog(Gambling(bot))
    bot.add_cog(Mathematics(bot))
    bot.add_cog(Administration(bot))
    bot.add_cog(News(bot))

    print("--- Cog Manager ---")
    for cog in bot.cogs:
        print(f"  Loaded: {cog}")
