import discord, aiohttp, feedparser
from discord.ext import commands

class News(commands.Cog, name='News'):
	# TODO Pass msg rm delay
	def __init__(self, bot):
		self.bot = bot
		self.rss_unboxholics = "https://unboxholics.com/news/gaming?format=rss"

	@commands.group()
	async def news(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("Specify news category")

	@news.command()
	async def games(self, ctx):

		d=feedparser.parse(self.rss_unboxholics)

		games_embed = discord.Embed(title="Game News")

		for entry in d.entries:

			games_embed.add_field(name=entry.title, value=entry.link, inline=False)

		await ctx.send(embed=games_embed)
			# print(20*'-')
			# print(entry.title)
