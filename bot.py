from sys import platform
import discord
from discord import activity
from discord.ext import commands
import logging
from pathlib import Path
import json
import platform
import os
import cogs._json
import aiohttp
from io import BytesIO
from discord import Activity, ActivityType
from discord.ext import tasks

import topgg

autoroles = {}

intents = discord.Intents.default()
intents.members = True

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n---")


def get_prefix(bot, message):
    data = cogs._json.read_json('prefixes')
    if not str(message.guild.id) in data:
        return commands.when_mentioned_or('.')(bot, message)
    return commands.when_mentioned_or(data[str(message.guild.id)])(bot, message)

secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix=get_prefix, intents = intents, case_insensitive = True)
bot.config_token = secret_file['token']

bot.blacklisted_users = []

bot.remove_command('help')

@bot.event
async def on_ready():
    global autoroles
    with open("autorole.json", "r") as f:
        autoroles = json.load(f)
    print(f"-----\n Logged in as: {bot.user.name} : {bot.user.id}\n-----\n Current prefix: -\n-----")
    data = read_json("blacklist")
    bot.blackListesUsers = data["blackListedUsers"]
    await bot.change_presence(activity=Activity(name=f"Ping me to get help || In {len(bot.guilds)} servers", 
                                                type=ActivityType.playing))

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if message.author.id in bot.blacklisted_users:
        return

    #this is for custom prefix
    if f"<@!{bot.user.id}>" in message.content:
        data = cogs._json.read_json('prefixes')
        if str(message.guild.id) in data:
            prefix = data[str(message.guild.id)]
        else:
            prefix = '.'
        prefixmsg= await message.channel.send(f"My prefix here is `{prefix}`\n\n Use `{prefix}help` to get help or join my support server by entering `{prefix}support`\n\n Also it would be a great help if you vote for me by typing `{prefix}vote` :D")
        await prefixmsg.add_reaction('👀')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, 
    id=autoroles[str(member.guild.id)])
    await member.add_roles(role)

def read_json(filename):
    with open(f"{cwd}/bot_config/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/bot_config/{filename}.json", "w") as file:
        json.dump(data, file, indent = 4)

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/moderation"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.moderation.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/errors"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.errors.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/webscraping"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.webscraping.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/misc"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.misc.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/currency"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.currency.{file[:-3]}")

if __name__ == '__main__':
    for file in os.listdir(cwd+"/cogs/fun"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.fun.{file[:-3]}")

@bot.command(aliases = ['ce', 'ae', 'addemoji'])
async def createemoji(ctx, url: str, *, name):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		async with aiohttp.ClientSession() as ses:
			async with ses.get(url) as r:
				
				try:
					img_or_gif = BytesIO(await r.read())
					b_value = img_or_gif.getvalue()
					if r.status in range(200, 299):
						emoji = await guild.create_custom_emoji(image=b_value, name=name)
						await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
						await ses.close()
					else:
						await ctx.send(f'Error when making request | {r.status} response.')
						await ses.close()
						
				except discord.HTTPException:
					await ctx.send('File size is too big!')

@bot.command()
async def deleteemoji(ctx, emoji: discord.Emoji):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted (or not): {emoji}')
		await emoji.delete()

#autorole starts from here

@bot.command()
@commands.has_permissions(administrator=True)
async def autorole(ctx, *, role : discord.Role=None):
  
  embed=discord.Embed(color=0x7289da, description=f"**Set autorole to** {role.mention}**?**")
  embed.set_footer(text="React with the wave reaction to confirm it!")
  msg = await ctx.send(embed=embed)

  def checkifnotbot(reaction, user):
      return user != bot.user

  await msg.add_reaction('👋')

  reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=checkifnotbot)

  if str(reaction.emoji) == "👋":   

    embedw=discord.Embed(description=f"👋**Autorole set!**\n> Everytime someone joins the server they get the {role.mention} role!", color=0x7289da)     
    await msg.edit(embed=embedw)
    await msg.clear_reactions()
    
    global autoroles
    autoroles[str(ctx.guild.id)] = role.id

    with open("autorole.json", "w") as f:
        json.dump(autoroles, f)

@tasks.loop(minutes=30)
async def update_stats():
    """This function runs every 30 minutes to automatically update your server count."""
    try:
        await bot.topggpy.post_guild_count()
        print(f"Posted server count ({bot.topggpy.guild_count})")
    except Exception as e:
        print(f"Failed to post server count\n{e.__class__.__name__}: {e}")


update_stats.start()

bot.run(bot.config_token)