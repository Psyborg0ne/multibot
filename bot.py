from discord.ext import commands

TOKEN = 'NzU3OTA3MTc4NzQzOTIyNzQ4.X2nOEA.6M8LmLB-zE4aOboTderx_Ejl1fY'
bot = commands.Bot(command_prefix='>')

@bot.command()
async def sqr(ctx, num):
    await ctx.send(int(num)** 2)

bot.run(TOKEN)
