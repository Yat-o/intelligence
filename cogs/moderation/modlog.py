import discord
from discord.ext import commands
import random
import json
import cogs._json

class Channels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True)
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def modlog(self, ctx):
        await ctx.channel.send("Invalid sub-command passes")


def setup(bot):
    bot.add_cog(Channels(bot))