from discord.ext import commands
import discord
import random, json

with open('config.json') as f:
    config = json.load(f)

random.seed()
bot = commands.Bot(command_prefix='>')

bot.add_cog(Gamble(bot))
bot.add_cog(MathCalc(bot))

for cog in bot.cogs:
    print(f"Loaded: {cog}")

bot.run(TOKEN)
