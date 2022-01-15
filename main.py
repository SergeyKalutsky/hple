import discord
from discord.ext import commands
from discord.utils import get
from api_token import TOKEN
from insult_api import is_insult
from db.db import log_message


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command('test')
async def ping(ctx):
    await ctx.send('testing')


async def mute_member(channels, member, mute):
    for channel in channels:
        for voice_member in channel.members:
            if member == voice_member:
                await member.edit(mute=mute)
                return

@bot.event
async def on_message(message):
   if message.author == bot.user:
       return
   res = is_insult(message.content)
   print(res)
   if res == 'Insult':
       log_message(message.content, message.author)
   await message.channel.send(res)


@bot.command('unmute')
async def mute(ctx, member: discord.Member = None):

    if member:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted_role)
        await member.send(f"You have been unmuted")
        await mute_member(ctx.guild.voice_channels, member, False)
    else:
        await ctx.send("Didn't work, try using the command *properly*")


@bot.command('mute')
async def mute(ctx, member: discord.Member = None):

    if member:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await member.send(f"You have been muted")
        await mute_member(ctx.guild.voice_channels, member, True)
    else:
        await ctx.send("Didn't work, try using the command *properly*")


@bot.command('muteall')
async def muteall(ctx):
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            await member.edit(mute=True)


@bot.command('unmuteall')
async def muteall(ctx):
    for channel in ctx.guild.voice_channels:
        for member in channel.members:
            await member.edit(mute=False)

bot.run(TOKEN)
