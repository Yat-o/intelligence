import discord
from discord.ext import commands
import random

class Channels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded")

    @commands.group(invoke_without_command = True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def new(self, ctx):
        await ctx.send("Invalid sub-command passes")

    @new.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def category(self, ctx, role: discord.Role, *, name):
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                      ctx.guild.me: discord.PermissionOverwrite(read_messages = True),
                      role : discord.PermissionOverwrite(read_messages = True)
                      }
        category = await ctx.guild.create_category(name = name, overwrites = overwrites)
        await ctx.send(f"Created category `{category.name}`")        

    @new.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def channel(self, ctx, role: discord.Role, *, name):
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                      ctx.guild.me: discord.PermissionOverwrite(read_messages = True),
                      role : discord.PermissionOverwrite(read_messages = True)
                      }
        channel = await ctx.guild.create_text_channel(name = name, overwrites = overwrites)
        await ctx.send(f"Created channel `{channel.name}`")   
        
def setup(bot):
    bot.add_cog(Channels(bot))