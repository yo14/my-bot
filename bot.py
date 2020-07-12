import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')

f = open("rules.txt","r")
rules = f.readlines()

filtered_words = ["cat","dog"]

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)


@client.command()
async def hello(ctx):
    await ctx.send('Hi testing')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You can't do that ;-;")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required args.")
        await ctx.message.delete()
    else:
        raise error

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
    try:
        await ctx.send(member.name + " has been banned from the community, because: " +reason)
    except:
        await ctx.send("The member has their dms closed.")

    await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " has been unbanned!")
            return

        await ctx.send(member+" was not found")

@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(729812183151804526)
    await member.add_roles(muted_role)
    await ctx.send(member.mention + " has been muted")


@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(729812183151804526)
    await member.remove_roles(muted_role)
    await ctx.send(member.mention + " has been unmuted")

client.run(TOKEN)
