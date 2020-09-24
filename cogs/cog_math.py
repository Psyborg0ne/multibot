class MathCalc(commands.Cog, name='Mathematics'):
	# TODO Pass msg rm delay
    def __init__(self, bot):
        self.bot = bot

    # TODO Add an eval function for quick mafs

    @commands.command()
	async def sqr(ctx, num):
    	await ctx.message.delete()
    	# TODO Use msg rm delay on send
    	await ctx.send(int(num)** 2, delete_after=5)