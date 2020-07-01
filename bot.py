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

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = "No reason provided"):
    await member.send("You have been kicked from RWID community, because: " +reason)
    await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "No reason provided"):
    await ctx.send(member.name + " has been banned from the community, because: " +reason)
    await member.ban(reason=reason)

@client.command(aliases=['u'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return

TOKEN = 'your_secret_token_put_here'

client.run(TOKEN)