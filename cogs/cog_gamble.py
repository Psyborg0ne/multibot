class Gamble(commands.Cog, name='Gambling'):
	# TODO Pass msg rm delay
    def __init__(self, bot):
        self.bot = bot

	@commands.command()
	async def flip(ctx):
		# TODO ? Maybe use global msg.delete on command invoke ?
	    await ctx.message.delete()
	    # TODO Flip for Emoji, need to construct Emojy object not shorthand e.g. :+1:
	    flip_embed = discord.Embed(title="FLIPPING MY NIGGA" ,
	    	description= f'**{ctx.message.author.name}** has flipped: {random.choice(["Heads" , "Tails"])}')
	    # TODO Use msg rm delay on send
	    await ctx.send(embed=flip_embed)

	@commands.command()
	async def roll(ctx, dice=1: int):
	    await ctx.message.delete()
	    if(1 <= dice < 10):
	        dice_embed = discord.Embed(title="Roll Machine" , description="Rolling")

	        for i in range(dice):
	            dice_embed.add_field(name=f"#{i+1}:" , value=random.randint(1,6) , inline=True)

	        await ctx.send(embed=kati)
	    else:
	        await ctx.send("Wrong usage, dice should be >= 1 and < 10")