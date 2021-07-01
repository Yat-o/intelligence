import discord
import asyncio
from discord.ext.commands.core import command
import requests
from discord.ext import commands

from googletrans import Translator
translator = Translator()

class trans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def translate(self, ctx, fro, to, *, text):
        translated = translator.translate(text, src=fro, dest=to)
        embed = discord.Embed(title="Translator", color=discord.Color.green())
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="From language", value=fro.capitalize(), inline=False)
        embed.add_field(name="What is being Translated", value=text, inline=False)
        embed.add_field(name="To Language", value=to.capitalize(), inline=False)
        embed.add_field(name="Translated Text", value=translated.text, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(trans(bot))
