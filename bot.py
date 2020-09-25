from discord.ext import commands
import utils
from cogs.cog_wallheaven import Wallheaven

config = utils.init()
bot = commands.Bot(command_prefix='>')
bot.add_cog(Wallheaven(bot, config["WH_API_KEY"]))
utils.loadCogs(bot)
bot.run(config["TOKEN"])
