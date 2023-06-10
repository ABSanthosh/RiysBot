import random
import discord
from discord.ext import commands
from discord import app_commands

limits = {
    "hug": 130,
    "kiss": 212,
    "blush": 40,
    "wave": 46,
    "pat": 127,
    "poke": 72,
    "bite": 40,
    "slap": 43
}


class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.baseUrl = "https://absanthosh.github.io/RiysBot/reactions/"
        self.reaction_messages = {
            "hug": [
                "hugs {user} tightly!",
                "gives a warm hug to {user}!",
                "wraps arms around {user} for a hug!"
            ],
            "kiss": [
                "gives a gentle kiss to {user}!",
                "plants a sweet kiss on {user}'s cheek!",
                "shares a passionate kiss with {user}!"
            ],
            "blush": [
                "blushes shyly!",
                "gets all flustered and blushes!",
                "can't help but blush!"
            ],
            "wave": [
                "waves excitedly at {user}!",
                "gives a friendly wave to {user}!",
                "waves at {user}!"
            ],
            "pat": [
                "gently pats {user}'s head!",
                "gives a comforting pat to {user}!",
                "pets {user} with affection!"
            ],
            "poke": [
                "pokes {user} playfully!",
                "gently taps {user} on the shoulder!",
                "boops {user}'s nose!"
            ],
            "bite": [
                "gives a playful bite to {user}!",
                "nibbles on {user}'s ear!",
                "playfully bites {user}'s arm!"
            ],
            "slap": [
                "slaps {user} with a feather!",
                "gives a gentle slap to {user}!",
                "playfully slaps {user} on the back!"
            ]
        }

    @app_commands.command(name="hug", description="Send a user a hug :3")
    async def hug(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["hug"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}hug/hug_{random.randint(1, limits['hug'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="kiss", description="Give the user a kiss mwah <3")
    async def kiss(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["kiss"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}kiss/kiss_{random.randint(1, limits['kiss'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="blush", description="Blush!")
    async def blush(self, ctx):
        message = random.choice(self.reaction_messages["blush"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}blush/blush_{random.randint(1, limits['blush'])}.gif")

        embed.add_field(name="", value=f"||{ctx.user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="wave", description="Wave at a user!")
    async def wave(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["wave"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}wave/wave_{random.randint(1, limits['wave'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="pat", description="Give user a headpat uwu")
    async def pat(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["pat"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}pat/pat_{random.randint(1, limits['pat'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="poke", description="Poke a user!")
    async def poke(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["poke"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}poke/poke_{random.randint(1, limits['poke'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="bite", description="Bite a user!")
    async def bite(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["bite"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}bite/bite_{random.randint(1, limits['bite'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="slap", description="Slap the shit out of a user! :p")
    async def slap(self, ctx, user: discord.Member):
        message = random.choice(self.reaction_messages["slap"])
        embed = discord.Embed(
            title=f"{ctx.user.name} {message.replace('{user}', user.name)}",
            color=discord.Color.random()
        )
        embed.set_image(
            url=f"{self.baseUrl}slap/slap_{random.randint(1, limits['slap'])}.gif")

        embed.add_field(
            name="", value=f"||{ctx.user.mention} {user.mention}||")
        await ctx.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Reactions(bot))
