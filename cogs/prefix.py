import discord
from discord.ext import commands 
import platform

from discord.ext.commands.core import command

import cogs._json

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["setprefix"])
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx, *, pre='.'):
        data = cogs._json.read_json('prefixes')
        data[str(ctx.message.guild.id)] = pre
        cogs._json.write_json(data, 'prefixes')
        await ctx.send(f"The guild prefix has been set to `{pre}` . Use `{pre}setprefix <prefix>` to change it again!")


def setup(bot):
    bot.add_cog(Commands(bot))