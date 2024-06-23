import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

TOKEN = 'MTI1MjY4NjE1MDk4MDYwMzk5NA.GImu0e.Ha1l9Vgc2kjKXQA5rmyS3d0JIVFefHh6hJheDc'

@bot.event
async def if_ready():
    print("Bot is ready to use")
    print("-------------------")

@bot.command()
async def hello(ctx):
    await ctx.send("Bitch!")

bot.run(TOKEN)
