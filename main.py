import discord
import os
from discord.ext import commands
from keep_alive import keep_alive


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

import random
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

baseUrl = "https://absanthosh.github.io/RiysBot/reactions/"

# a command for each reaction that takes a user as an argument and sends the reaction gif
# from the url of format baseUrl/{reaction}/{reaction}_{random number between 1 and limit for that reaction}.gif
@bot.command()
async def hug(ctx, user: discord.Member):
    await ctx.send(f"{ctx.author.mention} hugs {user.mention}! {baseUrl}hug/hug_{random.randint(1, limits['hug'])}.gif")

@bot.command()
async def kiss(ctx, user: discord.Member):
    await ctx.send(f"{ctx.author.mention} kisses {user.mention}! {baseUrl}kiss/kiss_{random.randint(1, limits['kiss'])}.gif")

@bot.command()
async def blush(ctx):
    await ctx.send(f"{ctx.author.mention} blushes! {baseUrl}blush/blush_{random.randint(1, limits['blush'])}.gif")

@bot.command()
async def wave(ctx):
    await ctx.send(f"{ctx.author.mention} waves! {baseUrl}wave/wave_{random.randint(1, limits['wave'])}.gif")

@bot.command()
async def pat(ctx, user: discord.Member):
    await ctx.send(f"{ctx.author.mention} pats {user.mention}! {baseUrl}pat/pat_{random.randint(1, limits['pat'])}.gif")

@bot.command()
async def poke(ctx, user: discord.Member):
    await ctx.send(f"{ctx.author.mention} pokes {user.mention}! {baseUrl}poke/poke_{random.randint(1, limits['poke'])}.gif")

@bot.command()
async def bite(ctx, user: discord.Member):
    await ctx.send(f"{ctx.author.mention} bites {user.mention}! {baseUrl}bite/bite_{random.randint(1, limits['bite'])}.gif")

@bot.command()
async def slap(ctx, user: discord.Member):
    await ctx.send(f"{ctx.author.mention} slaps {user.mention}! {baseUrl}slap/slap_{random.randint(1, limits['slap'])}.gif")


@bot.command()
async def hello(ctx):
    user_name = ctx.author.name 
    await ctx.send(f'Hello there {user_name}!')


keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))

