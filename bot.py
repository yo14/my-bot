import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

f = open("rules.txt","r")
rules = f.readlines()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def hello(ctx):
    await ctx.send('Hi testing')

@client.command(aliases=['rules','point'])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number) - 1])

TOKEN = 'put_your_token_here'

client.run(TOKEN)