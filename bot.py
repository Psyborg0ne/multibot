from discord.ext import commands
import random
import discord

random.seed()

bot = commands.Bot(command_prefix='>')

@bot.command()
async def sqr(ctx, num):
    await ctx.message.delete()
    await ctx.send(int(num)** 2)

@bot.command()
async def flip(ctx):
    await ctx.message.delete()
    flip_embed = discord.Embed(title="FLIPPING MY NIGGA" , description= f'**{ctx.message.author.name}** has flipped: {random.choice([":+1:" , ":-1:"])}')

    await ctx.send(embed=flip_embed)

@bot.command()
async def roll(ctx, dice=1):
    await ctx.message.delete()
    if(1 <= dice < 10):
        dice_embed = discord.Embed(title="Rolls" , description="Rolling")

        for i in range(int(dice)):
            dice_embed.add_field(name="Roll " +str(i+1) , value=random.randint(1,6) , inline=True)

        await ctx.send(embed=kati)
    else:
        await ctx.send("Wrong usage, dice should be >= 1 and < 10")


bot.run(TOKEN)
