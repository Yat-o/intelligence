import discord
from typing import Optional
from discord.ext import commands
from discord.ext.commands.core import command


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        """
        Load a cog or an extension.
        """
        try:
            self.bot.load_extension(cog)
            await ctx.send(":ok_hand: Cog Loaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")

    @commands.command(aliases=["logout"])
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
        """
        Logs this bot out.
        """

        await ctx.send("Logging out now\N{HORIZONTAL ELLIPSIS}")
        await ctx.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """Unload a cog or an extension."""
        try:
            self.bot.unload_extension(cog)
            await ctx.send(":ok_hand: Cog Unloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """Reload a cog or an extension."""
        try:
            self.bot.reload_extension(cog)
            await ctx.send(":ok_hand: Cog Reloaded")
        except commands.ExtensionError as e:
            await ctx.send(f"{e.__class__.__name__}: {e}")

    @commands.command()  # ill probably make these 2 commands public soon? say/embed
    @commands.has_permissions(manage_messages = True)
    async def say(self, ctx, *, msg):
        """Say something with the bot."""
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.is_owner()
    @commands.bot_has_permissions(embed_links=True)
    @commands.command()
    async def embed(self, ctx, color: Optional[discord.Color] = None, *, text):
        """
        Send an embed.
         """
        if color is None:
            color = await ctx.embed_color()
        embed = discord.Embed(description=text, color=color)
        if ctx.message.attachments:
            content = await ctx.message.attachments[0].to_file()
            embed.set_image(url="attachment://" + str(content.filename))
            await ctx.send(
            embed=embed, file=content if ctx.message.attachments else None
        )
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

    @commands.is_owner()
    @commands.guild_only()
    @commands.command(name="frick", aliases=["sho"], hidden=True)
    async def frick(self, ctx: commands.Context, limit: int = 50) -> None:
        """
        Cleans up the bots messages.
        `limit`: The amount of messages to check back through. Defaults to 50.
        """

        prefix = "."

        if ctx.channel.permissions_for(ctx.me).manage_messages:
            messages = await ctx.channel.purge(
                check=lambda message: message.author == ctx.me
                or message.content.startswith(prefix),
                bulk=True,
                limit=limit,
            )
        else:
            messages = await ctx.channel.purge(
                check=lambda message: message.author == ctx.me, bulk=False, limit=limit
            )

        await ctx.send(
            f"Found and deleted `{len(messages)}` of my message(s) out of the last `{limit}` message(s).",
            delete_after=3,
        )

    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)

        if command is None:
            await ctx.send("I cant find a command with that name")

        elif ctx.command == commands:
            await ctx.send("You cannot disable this command")

        else:
            
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"I have {ternary} {command}")
def setup(bot):
    bot.add_cog(Owner(bot))