import discord
import aiohttp  # requests are gey. dey blocking

import random



from discord.ext import commands
from discord.ext.commands.core import command

npa = ""  # default value for the args param if not passed in by a user


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # copy and pasting time bois
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, *, args):
        """Pats a user!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/pat") as r:

                pat = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} pats {args}", color=0x000000
                )
                embed.set_image(url=pat)
                await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx, *, args=npa):
        """Hug someone!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/hug") as r:

                hug = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} hugs {args}", color=0x000000
                )
                embed.set_image(url=hug)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx, *, args=npa):
        """Cuddle with someone!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/cuddle") as r:

                cuddle = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} cuddles {args}", color=0x000000
                )
                embed.set_image(url=cuddle)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx, *, args=npa):
        """Lick someone."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/lick") as r:

                lick = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} licks {args}", color=0x000000
                )
                embed.set_image(url=lick)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx, *, args=npa):
        """Bully someone :imp:"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/bully") as r:

                bully = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} bullies {args}", color=0x000000
                )
                embed.set_image(url=bully)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def poke(self, ctx, *, args=npa):
        """Boop Boop."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/poke") as r:

                poke = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} pokes {args}", color=0x000000
                )
                embed.set_image(url=poke)
                await ctx.send(embed=embed)

   

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx, *, args=npa):
        """Slap someone."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/slap") as r:

                slap = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} slaps {args}", color=0x000000
                )
                embed.set_image(url=slap)
                await ctx.send(embed=embed)

   
    @commands.command()
    @commands.guild_only()
    async def smug(self, ctx):
        """Be smug ig.."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/smug") as r:

                smug = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} has a smug look", color=0x000000
                )
                embed.set_image(url=smug)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx, *, args =npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/kiss") as r:

                kiss = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} kissed {args}")
                embed.set_image(url=kiss)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def cry(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/cry") as r:
                cry = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} is crying :(")
                embed.set_image(url=cry)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bonk(self, ctx, *, args = npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/bonk") as r:
                bonk = (await r.json()) ["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} bonked {args}")
                embed.set_image(url=bonk)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def yeet(self, ctx, *, args=npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/yeet") as r:
                yeet = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} yeeted {args}")
                embed.set_image(url=yeet)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def highfive(self, ctx, *, args=npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/highfive") as r:
                highfive = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} highfives {args}")
                embed.set_image(url=highfive)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def blush(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/blush") as r:
                blush = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} is blushing :>")
                embed.set_image(url=blush)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def smile(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/smile") as r:
                smile = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} is smiling aww :>")
                embed.set_image(url=smile)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def wave(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/wave") as r:
                wave = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} is waving... hii")
                embed.set_image(url=wave)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def happy(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/happy") as r:
                happy = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} is happy!")
                embed.set_image(url=happy)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def dance(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/dance") as r:
                dance = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} got some moves!")
                embed.set_image(url=dance)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def cringe(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/cringe") as r:
                cringe = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} cringed oww >:(")
                embed.set_image(url=cringe)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def nom(self, ctx):
        """Slap someone."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://waifu.pics/api/sfw/nom") as r:
                nom = (await r.json())["url"]

                embed = discord.Embed(
                    description=f"{ctx.author.mention} is eating", color=0x000000
                )
                embed.set_image(url=nom)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bite(self, ctx, *, args=npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/bite") as r:
                bite = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} bit {args}")
                embed.set_image(url=bite)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def glomp(self, ctx, *, args=npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/glomp") as r:
                glomp = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} glomps {args}")
                embed.set_image(url=glomp)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def kill(self, ctx, *, args=npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/kill") as r:
                kill = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} killed {args}")
                embed.set_image(url=kill)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def wink(self, ctx, *, args=npa):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.waifu.pics/sfw/wink") as r:
                wink = (await r.json())["url"]

                embed = discord.Embed(description=f"{ctx.author.mention} winked at {args}")
                embed.set_image(url=wink)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))