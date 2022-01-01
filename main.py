import discord
from discord.ext import commands
from api_token import TOKEN

bot = commands.Bot(command_prefix='$')

@bot.command('start')
async def ping(ctx):
    await ctx.send('hello world')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # message.author.id <-- user_id
    res = await bot.fetch_user(message.author.id)
    print(res)
    await message.channel.send('Hello!!!!!')

bot.run(TOKEN)
