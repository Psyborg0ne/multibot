import json, random
from cogs.cog_gamble import Gambling
from cogs.cog_math import Mathematics


def printLogo():
    with open("./res/logo.txt") as f:
        for i in f:
            print(i)


def init():
    printLogo()
    print("--- Init Phase ---")
    random.seed()
    print("  Random seed ok")
    with open('config.json') as f:
        config = json.load(f)
        print("  Config options set")
    return config

def loadCogs(bot):
    bot.add_cog(Gambling(bot))
    bot.add_cog(Mathematics(bot))

    print("--- Cog Manager ---")
    for cog in bot.cogs:
        print(f"  Loaded: {cog}")
