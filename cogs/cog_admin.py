import discord
from discord.ext import commands

class Administration(commands.Cog, name='Administration'):
	# TODO Pass msg rm delay
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def shout(self, ctx, *, msg: str):
		await ctx.message.delete()
		shout_embed = discord.Embed(title= "Important", description="@everyone", color= discord.Color(0xe30000))
		shout_embed.add_field(name=ctx.message.author.display_name, value= msg, inline=False)
		await ctx.send(embed = shout_embed, delete_after=5)
