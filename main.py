import discord
from discord.ext import commands
from discord.utils import get
from api_token import TOKEN
bot = commands.Bot(command_prefix='$')


@bot.command('test')
async def ping(ctx):
    await ctx.send('testing')


# @bot.event
# async def on_message(message):
#    if message.author == bot.user:
#        return
    # message.author.id <-- user_id
#    res = await bot.fetch_user(message.author.id)
#    print(res)
#    await message.channel.send('Hello!!!!!')

@bot.command('unmute')
async def mute(ctx, member: discord.Member = None):

    if member:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted_role)
        await member.send(f"You have been unmuted")
    else:
        await ctx.send("Didn't work, try using the command *properly*")


@bot.command('mute')
async def mute(ctx, member: discord.Member = None):

    if member:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await member.send(f"You have been muted")
    else:
        await ctx.send("Didn't work, try using the command *properly*")


bot.run(TOKEN)
