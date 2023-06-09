import random
import discord
from discord.ext import commands
from discord import app_commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Ping the bot!")
    async def ping(self, ctx):
        await ctx.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")


async def setup(bot):
    await bot.add_cog(Ping(bot))
