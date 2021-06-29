import discord
from discord import colour
from discord import embeds
from discord.asset import VALID_AVATAR_FORMATS
from discord.ext import commands 
import platform
import DiscordUtils

from discord.ext.commands.core import command
from discord.mixins import EqualityComparable

import cogs._json

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        embed = discord.Embed(title= "**Help commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name= "**Moderation**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Misc**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Currency**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Fun**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Config**", value= "\uFEFF", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}. Also consider voting for me by typing <your prefix>vote :D")
        await ctx.send(embed = embed)

    @help.command(aliases = ["mod"])
    async def moderation(self, ctx):
        embed = discord.Embed(title= "**Moderation commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name=f"**Warn**", value= "Warns a member with the provided reason \uFEFF", inline= False)
        embed.add_field(name=f"**Warns**", value= "Gives warnings received by the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Removewarn**", value= "Removes specified warn for the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Kick**", value="Kicks the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Ban**", value="Bans the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Unban**", value="Unban a user using their ID \uFEFF", inline= False)
        embed.add_field(name=f"**Clear**", value="Purge mentioned amount of messages \uFEFF", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command(aliases = ["miscellaneous"])
    async def misc(self, ctx):
        embed = discord.Embed(title= "**Miscellaneous commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name = "**Stats**", value="Get stats about me", inline= False)
        embed.add_field(name = "**Ping**", value="Get bots ping", inline= False)
        embed.add_field(name = "**Serverinfo**", value="Get info about the guild", inline= False)
        embed.add_field(name = "**Userinfo**", value="Get info about the mentioned user", inline= False)
        embed.add_field(name = "**Roleinfo**", value="Get info about the specified role", inline= False)
        embed.add_field(name = "**Remind**", value="Set a reminder", inline= False)
        embed.add_field(name = "**Support**", value="Join my support server", inline= False)
        embed.add_field(name = "**Poll**", value="Make a simple poll", inline= False)
        embed.add_field(name = "**User**", value="Get a user's avatar", inline= False)
        embed.add_field(name = "**Server**", value="Get the server's avatar", inline= False)
        embed.add_field(name = "**Weather**", value="Show weather of a specified city/state", inline= False)
        embed.add_field(name = "**Covid**", value="Show covid-19 statistics about a specified *country*", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command()
    async def currency(self, ctx):
        embed = discord.Embed(title= "**Currency commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name = "**Inventory**", value="Show your Inventory", inline= False)
        embed.add_field(name = "**Balance**", value="Get your balance", inline= False)
        embed.add_field(name = "**Beg**", value="Beg for money", inline= False)
        embed.add_field(name = "**Deposit**", value="Deposit a specified amount of money in the bank", inline= False)
        embed.add_field(name = "**Withdraw**", value="Withdraw a specified amount of money from the bank", inline= False)
        embed.add_field(name = "**Send**", value="Send a specified amount of money to a user", inline= False)
        embed.add_field(name = "**Slots**", value="Play slots", inline= False)
        embed.add_field(name = "**Rob**", value="Rob a user", inline= False)
        embed.add_field(name = "**Shop**", value="Show the shop", inline= False)
        embed.add_field(name = "**Buy**", value="Buy an item from the shop", inline= False)
        embed.add_field(name = "**Sell**", value="Sell an item from your Inventory", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command()
    async def fun(self, ctx):
        embed = discord.Embed(title= "**Fun commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name = "**Roleplay**", value="Show a list of roleplay commands!", inline= False)
        embed.add_field(name = "**Fact**", value="Show a list of fact commands!", inline= False)
        embed.add_field(name = "**Compliment**", value="Compliment someone", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command()
    async def config(self, ctx):
        embed = discord.Embed(title= "**Fun commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name= "**Setprefix**", value= "Set a prefix for your guild")
        embed.add_field(name=f"**Autorole**", value="Add a role as your autorole for the guild \uFEFF", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command(aliases = ["rp"])
    async def roleplay(self, ctx):
        embed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Pat - Pat a user\n\nHug - Hug a user\n\nCuddle - Cuddle with a user\n\nLick - Lick a user\n\nBully - Bully a user", value="Page 1")
        embed2 = discord.Embed(color=ctx.author.color).add_field(name=f"Poke - Poke a user\n\nSlap - Slap a user\n\nSmug - Give a smug look\n\nKiss - Kiss a user\n\nCry - Cry", value="Page 2")
        embed3 = discord.Embed(color=ctx.author.color).add_field(name=f"Bonk - Bonk a user\n\nYeet - Yeet a user\n\nHighfive - HighFive a user\n\nBlush - Blush uwu\n\nSmile - Smile", value="Page 3")
        embed4 = discord.Embed(color=ctx.author.color).add_field(name=f"Wave - Wave o/\n\nHappy - Be happy\n\nDance - Dance\n\nCringe - Cringe ig", value="Page 4")
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('🔐', "lock")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [embed1, embed2, embed3, embed4]
        await paginator.run(embeds)

    @help.command(aliases = ["facts"])
    async def fact(self, ctx):
        embed = discord.Embed(title= "**Fun commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name= "**Catfact**", value= "Get a random cat fact")
        embed.add_field(name= "**Dogfact**", value= "Get a random dog fact")
        embed.add_field(name= "**Pandafact**", value= "Get a random panda fact")
        embed.add_field(name= "**Birdfact**", value= "Get a random bird fact")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(help(bot))