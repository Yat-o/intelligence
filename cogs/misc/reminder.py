import discord
from discord.ext import commands
import asyncio

class Remind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(alises = ['r'])
    async def remind(self, ctx, time, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2

            return val * time_dict[unit]

        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send("You didnt specify the time correctly")
            return

        if converted_time ==-2:
            await ctx.send("The time must be in integers")
            return

        embed = discord.Embed(description="Timer")
        embed.add_field(name="Reminder set", value=f"Started reminder for **{task}** and will last **{time}**")
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

        await asyncio.sleep(converted_time)
        await ctx.send(f"{ctx.author.mention}! Your reminder for **{task}** has finished!")

def setup(bot):
    bot.add_cog(Remind(bot))