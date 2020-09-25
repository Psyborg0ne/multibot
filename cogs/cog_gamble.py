import discord, random
from discord.ext import commands

class Gambling(commands.Cog, name='Gambling'):
	# TODO Pass msg rm delay
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def flip(self,ctx):
		# TODO ? Maybe use global msg.delete on command invoke ?
		await ctx.message.delete()
		# TODO Flip for Emoji, need to construct Emojy object not shorthand e.g. :+1:
		flip_embed = discord.Embed(title="FLIPPING MY NIGGA" ,
			description= f'**{ctx.message.author.name}** has flipped: {random.choice(["Heads" , "Tails"])}')
		# TODO Use msg rm delay on send
		await ctx.send(embed=flip_embed)

	@commands.command()
	async def roll(self, ctx, dice: int= 1):
		await ctx.message.delete()
		if(1 <= dice < 10):
			dice_embed = discord.Embed(title="Roll Machine" , description="Rolling")

			for i in range(dice):
				dice_embed.add_field(name=f"Roll #{i+1}:" , value=random.randint(1,6) , inline=True)

			await ctx.send(embed=dice_embed)
		else:
			await ctx.send("Wrong usage, dice should be >= 1 and < 10")
