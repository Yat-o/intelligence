import discord
import aiohttp
import randfacts

from discord.ext import commands

x = randfacts.getFact()


class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def catfact(self, ctx):
        """Get a random cat fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/cat') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def dogfact(self, ctx):
        """Get a random dog fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/dog') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def pandafact(self, ctx):
        """Get a random panda fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/panda') as r:
                await ctx.send((await r.json())['fact'])

    @commands.command()
    async def birdfact(self, ctx):
        """Get a random bird fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/facts/bird') as r:
                await ctx.send((await r.json())['fact'])


    @commands.command()
    async def random(self, ctx):
        """Get a random fact"""
        await ctx.send(x)


def setup(bot):
    bot.add_cog(Facts(bot))