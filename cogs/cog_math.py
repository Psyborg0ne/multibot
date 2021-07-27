from discord.ext import commands


class Mathematics(commands.Cog, name="Mathematics"):
    # TODO Pass msg rm delay
    def __init__(self, bot):
        self.bot = bot

    # TODO Add an eval function for quick mafs

    @commands.command()
    async def sqr(self, ctx, num: int):
        await ctx.message.delete()
        # TODO Use msg rm delay on send
        await ctx.send(num ** 2, delete_after=5)
