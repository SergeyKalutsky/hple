import discord
from discord.ext import commands
from api_token import TOKEN

bot = commands.Bot(command_prefix='$')

@bot.command('start')
async def ping(ctx):
    await ctx.send('hello world')

bot.run(TOKEN)
