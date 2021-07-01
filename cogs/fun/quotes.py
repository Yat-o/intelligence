import discord
import aiohttp
import randfacts
import io
from io import BytesIO
from discord.ext import commands


class quote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        """Get a random anime quote"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animu/quote') as r:
                embed = discord.Embed(title= "Quotes", description = "Get random anime quotes", colour = ctx.author.colour)
                embed.add_field(name="Quote:", value=(await r.json())['sentence'], inline = False)
                embed.add_field(name="Said by:", value=(await r.json())['characther'], inline = True)
                embed.add_field(name="In:", value=(await r.json())['anime'], inline = True)
                await ctx.send(embed =embed)

def setup(bot):
    bot.add_cog(quote(bot))