import discord
from discord.ext import commands
import asyncio
import json
import aiohttp
import datetime
import random
import io
class pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pokedex(self, ctx, *, pokedex=None):
        """A simple poxedex command"""
        await ctx.trigger_typing()

        if pokedex is None:
            await ctx.reply('You didnt entered anything...') # or ctx.send
            
        pokesession = aiohttp.ClientSession()
        pokeget = await pokesession.get(f'https://some-random-api.ml/pokedex?pokemon={pokedex}')
        pokeresp = json.loads(await pokeget.text())

        name = pokeresp['name']
        pokeid = pokeresp['id'] # using pokeid instead of id because pylint will give some warning lol, but its your choice, nothing will happen if the variables name is id, it doesnt really matter
        poketype = pokeresp['type']
        specie = pokeresp['species']
        abilities = pokeresp['abilities']
        height = pokeresp['height']
        weight = pokeresp['weight']
        base_exp = pokeresp['base_experience']
        gender = pokeresp['gender']
        hp = pokeresp['stats']['hp']
        attack = pokeresp['stats']['attack']
        defense = pokeresp['stats']['defense']
        sp_atk = pokeresp['stats']['sp_atk']
        sp_def = pokeresp['stats']['sp_def']
        speed = pokeresp['stats']['speed']
        total = pokeresp['stats']['total']

        image = pokeresp['sprites']['normal']
        imageanimated = pokeresp['sprites']['animated']

        embed = discord.Embed(title=f'Information about **{name}**', color=discord.Color.blurple())
        embed.add_field(name='Name', value=f'**{name}**')
        embed.add_field(name='ID', value=f'**{pokeid}**')
        embed.add_field(name='Type', value=f'**{poketype}**')
        embed.add_field(name='Species', value=f'**{specie}**')
        embed.add_field(name='Abilities', value=f'**{abilities}**')
        embed.add_field(name='Height', value=f'**{height}**')
        embed.add_field(name='Weight', value=f'**{weight}**')
        embed.add_field(name='Base Experience', value=f'**{base_exp}**')
        embed.add_field(name='Gender', value=f'**{gender}**')
        embed.add_field(name='HP', value=f'**{hp}**')
        embed.add_field(name='Attack', value=f'**{attack}**')
        embed.add_field(name='Defense', value=f'**{defense}**')
        embed.add_field(name='SP Attack', value=f'**{sp_atk}**')
        embed.add_field(name='SP Defense', value=f'**{sp_def}**')
        embed.add_field(name='Speed', value=f'**{speed}**')
        embed.add_field(name='Total', value=f'**{total}**')

        embed.set_thumbnail(url=image) # image, non animated. will be shown at the top right side of the embed
        embed.set_image(url=imageanimated) # gif, will be show inside the embed

        await pokesession.close()

        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(pokemon(bot))