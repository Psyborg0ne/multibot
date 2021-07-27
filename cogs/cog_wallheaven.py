import discord
import aiohttp

from discord.ext import commands


class Wallheaven(commands.Cog, name="Wallheaven"):
    # TODO Pass msg rm delay
    def __init__(self, bot, apiKey):
        self.bot = bot
        self.page = 1
        self.apiKey = apiKey
        self.base_url = "https://wallhaven.cc/api/v1/search?"
        self.payload = {
            "apikey": self.apiKey,
            "purity": "001",
            "categories": "001",
            "atleast": "1920x1080",
            "page": self.page,
        }

    @commands.command()
    async def porn(self, ctx, num: int = 1):
        if num > 24:
            self.payload["page"] = num // 24
            num %= 24
        else:
            self.payload["page"] = 1
            num = num

        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=self.payload) as r:
                if r.status == 200:
                    js = await r.json()
                    pic = js["data"][num - 1]["path"]
                    wh_embed = discord.Embed(
                        title="Straight outta WH", color=discord.Color(0xE30000)
                    )
                    wh_embed.set_image(url=pic)
                    await ctx.send(embed=wh_embed)
