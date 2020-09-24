from discord.ext import commands
import utils

config = utils.init()
bot = commands.Bot(command_prefix='>')
utils.loadCogs(bot)
bot.run(config["TOKEN"])
