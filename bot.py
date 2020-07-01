import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def hello(ctx):
    await ctx.send('Hi testing')

TOKEN = 'put_your_token_here'

client.run(TOKEN)