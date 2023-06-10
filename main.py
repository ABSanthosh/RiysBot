import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

from commands.reactions import Reactions
from commands.eightball import EightBall
from commands.cuteometer import CuteOMeter
from commands.ping import Ping


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="with your heart"))
    await bot.change_presence(status=discord.Status.online)

    await bot.load_extension("commands.reactions")
    await bot.load_extension("commands.eightball")
    await bot.load_extension("commands.cuteometer")
    await bot.load_extension("commands.ping")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {synced} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")
        


keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))
