import discord
import aiohttp  # requests are gey. dey blocking
import random
  
from random import choice, randint

from discord.ext import commands
from discord.ext.commands.core import command

class compliment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def compliment(self, ctx: commands.Context, member: discord.Member = None):
        """Compliment someone or yourself"""
        if member is None:
            member = ctx.author

        compliments = [
            "Your positivity is infectious.",
            "You should be so proud of yourself.",
            "You’re amazing!",
            "You’re a true gift to the people in your life.",
            "You’re an incredible friend.",
            "I really appreciate everything that you do.",
            "You inspire me to be a better person.",
            "Your passion always motivates me.",
            "Your smile makes me smile.",
            "Thank you for being such a great person.",
            "The way you carry yourself is truly admirable.",
            "You are such a good listener.",
            "You have a remarkable sense of humor.",
            "Thanks for being you!",
            "You set a great example for everyone around you.",
            "I love your perspective on life.",
            "Being around you makes everything better.",
            "You always know the right thing to say.",
            "The world would be a better place if more people were like you!",
            "You are one of a kind.",
            "You make me want to be the best version of myself.",
            "You always have the best ideas.",
            "I’m so lucky to have you in my life.",
            "Your capacity for generosity knows no bounds.",
            "I wish I were more like you.",
            "You are so strong.",
            "I’ve never met someone as kind as you are.",
            "You have such a great heart.",
            "Simply knowing you has made me a better person.",
            "You are beautiful inside and out.",
        ]
        await ctx.send(
            embed=discord.Embed(
                description=f"{member.mention} {choice(compliments)}",
                colour = ctx.author.colour
            ).set_footer(text=f"From {ctx.author}")
        )


def setup(bot):
    bot.add_cog(compliment(bot))