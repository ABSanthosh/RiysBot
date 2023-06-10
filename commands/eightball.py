import random
import discord
from discord import app_commands
from discord.ext import commands


class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

    @app_commands.command(name="8ball", description="Ask the magic 8ball a question!")
    async def eightball(self, ctx, *, question: str):
        response = random.choice(self.responses)
        await ctx.response.send_message(f"Question: {question}\nAnswer: {response}")


async def setup(bot):
    await bot.add_cog(EightBall(bot))