import random
import discord
from discord.ext import commands
from discord import app_commands


class CuteOMeter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.phrases = [
            "is absolutely precious!",
            "is just so adorable!",
            "brings out the cuteness in everything!",
            "is unbelievably cute!",
            "is the epitome of cuteness!",
            "is adorable beyond words!",
            "makes the world a cuter place!",
            "is too cute to handle!",
            "are absolutely precious!",
            "is cute as a button!",
            "'s cuteness is off the charts!"
        ]

    @app_commands.command(name="cute", description="How cute are you?")
    async def cute(self, ctx, user: discord.Member):
        cute_level = random.randint(80, 100)
        phrase = random.choice(self.phrases)
        mention = user.mention
        name = user.name
        embed = discord.Embed(title="Cute-O-Meter", description=f"{mention} {phrase}", color=0x00ff00)
        await ctx.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(CuteOMeter(bot))
