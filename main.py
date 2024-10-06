import discord

from config import TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def if_ready():
    print("Bot is ready to use")
    print("-------------------")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
